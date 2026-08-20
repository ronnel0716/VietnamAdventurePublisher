r"""
Publish a polished copy of a Vietnam Adventure handbook.

Usage:
    .\.venv\Scripts\python.exe tools\publish_handbook.py `
        "handbook\source\Vietnam Adventure 2026 Handbook.docx"
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_FOLDER = ROOT / "output"

CHAPTER_PATTERN = re.compile(
    r"^CHAPTER\s+(\d+)\s*$",
    re.IGNORECASE,
)

NAVY = RGBColor(21, 58, 86)
TEAL = RGBColor(0, 124, 146)
CHARCOAL = RGBColor(45, 52, 58)


def set_run_font(run, name, size, color, bold=False):
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold


def configure_styles(document):
    for section in document.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.85)
        section.right_margin = Inches(0.85)

    normal = document.styles["Normal"]
    normal.font.name = "Aptos"
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Aptos")
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = CHARCOAL
    normal.paragraph_format.space_after = Pt(7)
    normal.paragraph_format.line_spacing = 1.15

    title = document.styles["Title"]
    title.font.name = "Aptos Display"
    title._element.rPr.rFonts.set(qn("w:eastAsia"), "Aptos Display")
    title.font.size = Pt(28)
    title.font.bold = True
    title.font.color.rgb = NAVY
    title.paragraph_format.space_after = Pt(18)

    subtitle = document.styles["Subtitle"]
    subtitle.font.name = "Aptos"
    subtitle._element.rPr.rFonts.set(qn("w:eastAsia"), "Aptos")
    subtitle.font.size = Pt(12)
    subtitle.font.bold = True
    subtitle.font.color.rgb = TEAL
    subtitle.paragraph_format.space_before = Pt(4)
    subtitle.paragraph_format.space_after = Pt(10)
    subtitle.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    heading_1 = document.styles["Heading 1"]
    heading_1.font.name = "Aptos Display"
    heading_1._element.rPr.rFonts.set(qn("w:eastAsia"), "Aptos Display")
    heading_1.font.size = Pt(20)
    heading_1.font.bold = True
    heading_1.font.color.rgb = NAVY
    heading_1.paragraph_format.space_before = Pt(18)
    heading_1.paragraph_format.space_after = Pt(10)
    heading_1.paragraph_format.keep_with_next = True

    heading_2 = document.styles["Heading 2"]
    heading_2.font.name = "Aptos Display"
    heading_2._element.rPr.rFonts.set(qn("w:eastAsia"), "Aptos Display")
    heading_2.font.size = Pt(15)
    heading_2.font.bold = True
    heading_2.font.color.rgb = TEAL
    heading_2.paragraph_format.space_before = Pt(14)
    heading_2.paragraph_format.space_after = Pt(7)
    heading_2.paragraph_format.keep_with_next = True

    heading_3 = document.styles["Heading 3"]
    heading_3.font.name = "Aptos"
    heading_3._element.rPr.rFonts.set(qn("w:eastAsia"), "Aptos")
    heading_3.font.size = Pt(12)
    heading_3.font.bold = True
    heading_3.font.color.rgb = NAVY
    heading_3.paragraph_format.space_before = Pt(10)
    heading_3.paragraph_format.space_after = Pt(5)
    heading_3.paragraph_format.keep_with_next = True


def add_page_number(paragraph):
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), "PAGE")
    paragraph._p.append(field)


def configure_headers_and_footers(document):
    for section in document.sections:
        section.different_first_page_header_footer = True

        # Keep the cover page deliberately clean.
        section.first_page_header.paragraphs[0].text = ""
        section.first_page_footer.paragraphs[0].text = ""

        header = section.header.paragraphs[0]
        header.text = "VIETNAM ADVENTURE 2026"
        header.alignment = WD_ALIGN_PARAGRAPH.RIGHT

        for run in header.runs:
            set_run_font(run, "Aptos", 8, TEAL, bold=True)

        footer = section.footer.paragraphs[0]
        footer.text = "Vietnam Adventure 2026 Handbook  |  Page "
        footer.alignment = WD_ALIGN_PARAGRAPH.CENTER

        for run in footer.runs:
            set_run_font(run, "Aptos", 8, CHARCOAL)

        add_page_number(footer)


def find_first_content_paragraph(document):
    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            return paragraph

    return None


def create_cover_subtitle(document, title_paragraph):
    """Add a restrained subtitle beneath the cover title."""
    subtitle = create_paragraph_element(
        "TRAVEL HANDBOOK",
        style_id=document.styles["Subtitle"].style_id,
    )

    title_paragraph._p.addnext(subtitle)
    return subtitle


def style_chapters(document):
    chapter_count = 0

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        if not CHAPTER_PATTERN.fullmatch(text):
            continue

        paragraph.style = document.styles["Heading 1"]

        if chapter_count > 0:
            paragraph.paragraph_format.page_break_before = True

        chapter_count += 1

    return chapter_count


def normalize_existing_headings(document):
    """
    Keeps only real CHAPTER 1–16 markers as Heading 1.

    Labels such as 'CHAPTER 4 – Block 2' become Heading 2,
    preventing them from appearing in the Table of Contents.
    """
    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        if CHAPTER_PATTERN.fullmatch(text):
            paragraph.style = document.styles["Heading 1"]
            continue

        if paragraph.style.name == "Heading 1":
            paragraph.style = document.styles["Heading 2"]

        if paragraph.style.name in {"Heading 1", "Heading 2", "Heading 3"}:
            paragraph.paragraph_format.keep_with_next = True


def create_paragraph_element(text="", style_id=None):
    paragraph = OxmlElement("w:p")

    if style_id:
        properties = OxmlElement("w:pPr")
        style = OxmlElement("w:pStyle")
        style.set(qn("w:val"), style_id)
        properties.append(style)
        paragraph.append(properties)

    if text:
        run = OxmlElement("w:r")
        text_element = OxmlElement("w:t")
        text_element.text = text
        run.append(text_element)
        paragraph.append(run)

    return paragraph


def create_toc_field_element():
    paragraph = OxmlElement("w:p")

    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), r'TOC \o "1-1" \h \z \u')

    run = OxmlElement("w:r")
    text = OxmlElement("w:t")
    text.text = "Right-click here and choose Update Field."
    run.append(text)
    field.append(run)

    paragraph.append(field)
    return paragraph


def create_page_break_element():
    paragraph = OxmlElement("w:p")
    run = OxmlElement("w:r")
    page_break = OxmlElement("w:br")
    page_break.set(qn("w:type"), "page")
    run.append(page_break)
    paragraph.append(run)
    return paragraph


def insert_table_of_contents(document, title_paragraph):
    """Insert a TOC on its own page after the cover."""
    anchor = getattr(title_paragraph, "_p", title_paragraph)
    cover_page_break = create_page_break_element()

    toc_heading = create_paragraph_element(
        "Table of Contents",
        style_id="TOCHeading",
    )
    toc_field = create_toc_field_element()
    toc_page_break = create_page_break_element()

    anchor.addnext(cover_page_break)
    cover_page_break.addnext(toc_heading)
    toc_heading.addnext(toc_field)
    toc_field.addnext(toc_page_break)

    settings = document.settings.element

    for existing in settings.findall(qn("w:updateFields")):
        settings.remove(existing)

    update_fields = OxmlElement("w:updateFields")
    update_fields.set(qn("w:val"), "true")
    settings.append(update_fields)


def publish(source, destination):
    if not source.exists():
        raise FileNotFoundError(f"Source handbook not found: {source}")

    document = Document(source)

    configure_styles(document)
    configure_headers_and_footers(document)

    title_paragraph = find_first_content_paragraph(document)
    title = "Vietnam Adventure 2026 Handbook"

    if title_paragraph is not None:
        title = title_paragraph.text.strip()
        title_paragraph.style = document.styles["Title"]
        title_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        title_paragraph.paragraph_format.space_before = Pt(170)

        cover_anchor = create_cover_subtitle(document, title_paragraph)
    else:
        cover_anchor = None

    chapter_count = style_chapters(document)
    normalize_existing_headings(document)

    if cover_anchor is not None:
        insert_table_of_contents(document, cover_anchor)

    destination.parent.mkdir(parents=True, exist_ok=True)
    document.save(destination)

    return title, chapter_count


def main():
    parser = argparse.ArgumentParser(
        description="Create a polished DOCX handbook from a source DOCX."
    )
    parser.add_argument(
        "source",
        type=Path,
        help="Path to the source handbook DOCX.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional output DOCX path.",
    )
    args = parser.parse_args()

    source = args.source.resolve()

    if args.output is None:
        destination = (
            DEFAULT_OUTPUT_FOLDER
            / f"{source.stem} - Published.docx"
        )
    else:
        destination = args.output.resolve()

    if source == destination:
        print("Error: output path must differ from the source file.")
        return 1

    print("=" * 60)
    print("Vietnam Adventure Publisher")
    print("Handbook Publishing")
    print("=" * 60)
    print(f"\nSource : {source}")

    title, chapter_count = publish(source, destination)

    print(f"Title  : {title}")
    print(f"Chapters styled : {chapter_count}")
    print(f"\nPublished handbook created:\n{destination}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
