#!/usr/bin/env python3
"""Create a human-test XLSX without dependencies or SAP connectivity."""

import argparse
import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZIP_DEFLATED, ZipFile


NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
XML = "http://www.w3.org/XML/1998/namespace"
META = ("story_id", "alm_revision", "spec_revision", "system_client", "target_objects")
FIELDS = ("id", "coverage", "scenario", "preconditions", "steps", "expected")
INVALID_XML = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\ud800-\udfff\ufffe\uffff]")
HEADERS = (
    "Test ID", "Criterion / regression reason", "Scenario", "Preconditions",
    "Inputs / human steps", "Expected result", "Actual result", "Status",
    "Evidence reference", "Tester", "Execution date", "Actual tested object/version",
)


def validate(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be a JSON object.")
    if set(data) != set(META) | {"cases"}:
        raise ValueError("Input fields must match the test-cases template.")
    for key in META:
        validate_text(data[key], key)
    if not isinstance(data["cases"], list) or not data["cases"]:
        raise ValueError("cases must be a nonempty list.")
    if len(data["cases"]) > 1048575:
        raise ValueError("Too many cases for one Excel worksheet.")
    seen = set()
    for index, case in enumerate(data["cases"], 1):
        if not isinstance(case, dict) or set(case) != set(FIELDS):
            raise ValueError(f"Case {index} fields must match the template.")
        for key in FIELDS:
            validate_text(case[key], f"Case {index}: {key}")
        if case["id"] in seen:
            raise ValueError(f"Duplicate test ID: {case['id']}")
        seen.add(case["id"])


def validate_text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a nonempty string.")
    if len(value) > 32767 or INVALID_XML.search(value):
        raise ValueError(f"{label} contains text Excel cannot represent.")
    if re.search(r"<[^>]+>", value):
        raise ValueError(f"{label} contains an unresolved angle-bracket placeholder.")


def xml_bytes(element):
    return ET.tostring(element, encoding="utf-8", xml_declaration=True)


def column_name(number):
    result = ""
    while number:
        number, remainder = divmod(number - 1, 26)
        result = chr(65 + remainder) + result
    return result


def worksheet(rows, widths, autofilter=False):
    root = ET.Element("worksheet", xmlns=NS)
    views = ET.SubElement(root, "sheetViews")
    view = ET.SubElement(views, "sheetView", workbookViewId="0")
    ET.SubElement(view, "pane", ySplit="1", topLeftCell="A2", state="frozen")
    columns = ET.SubElement(root, "cols")
    for number, width in enumerate(widths, 1):
        ET.SubElement(columns, "col", min=str(number), max=str(number),
                      width=str(width), customWidth="1")
    sheet_data = ET.SubElement(root, "sheetData")
    for row_number, values in enumerate(rows, 1):
        row = ET.SubElement(sheet_data, "row", r=str(row_number))
        for col_number, value in enumerate(values, 1):
            cell = ET.SubElement(
                row, "c", r=f"{column_name(col_number)}{row_number}", t="inlineStr"
            )
            text = ET.SubElement(ET.SubElement(cell, "is"), "t")
            text.set(f"{{{XML}}}space", "preserve")
            text.text = value
    if autofilter:
        ET.SubElement(root, "autoFilter",
                      ref=f"A1:{column_name(len(rows[0]))}{len(rows)}")
    return xml_bytes(root)


def write_workbook(data, output):
    tests = [HEADERS]
    tests.extend(
        [case[field] for field in FIELDS]
        + ["", "Not executed", "", "", "", ""]
        for case in data["cases"]
    )
    metadata = [("Field", "Value")]
    metadata.extend((key, data[key]) for key in META)
    metadata.extend([
        ("Purpose", "Proposed test cases for human execution; not execution evidence."),
        ("Target metadata", "Intended target; record actual version after execution."),
        ("AI execution", "Program and tests were not executed by AI."),
    ])
    workbook = ET.Element("workbook", xmlns=NS)
    sheets = ET.SubElement(workbook, "sheets")
    for number, name in enumerate(("Tests", "Metadata"), 1):
        ET.SubElement(sheets, "sheet", name=name, sheetId=str(number),
                      attrib={f"{{{REL}}}id": f"rId{number}"})
    relationships = ET.Element(
        "Relationships",
        xmlns="http://schemas.openxmlformats.org/package/2006/relationships",
    )
    for number in (1, 2):
        ET.SubElement(relationships, "Relationship", Id=f"rId{number}",
                      Type=f"{REL}/worksheet", Target=f"worksheets/sheet{number}.xml")
    content_types = b"""<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
<Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
</Types>"""
    root_rels = b"""<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>"""
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("xb") as target:
        with ZipFile(target, "w", ZIP_DEFLATED) as archive:
            archive.writestr("[Content_Types].xml", content_types)
            archive.writestr("_rels/.rels", root_rels)
            archive.writestr("xl/workbook.xml", xml_bytes(workbook))
            archive.writestr("xl/_rels/workbook.xml.rels", xml_bytes(relationships))
            archive.writestr("xl/worksheets/sheet1.xml",
                             worksheet(tests, (14, 30, 35, 40, 50, 50, 50, 18,
                                               35, 20, 20, 40), autofilter=True))
            archive.writestr("xl/worksheets/sheet2.xml", worksheet(metadata, (25, 100)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.output.suffix.lower() != ".xlsx":
            raise ValueError("Output must have an .xlsx extension.")
        data = json.loads(args.input.read_text(encoding="utf-8"))
        validate(data)
        write_workbook(data, args.output)
    except (OSError, ValueError) as error:
        print(f"Workbook creation failed: {error}", file=sys.stderr)
        return 1
    print(f"Created {args.output} with {len(data['cases'])} unexecuted test cases.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
