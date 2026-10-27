"""Small, runnable DOCX-to-HTML/JSON portfolio pipeline.

Only paragraphs, heading styles and table cell text are supported. This is
deliberately separate from the unfinished semantic/publishing scaffold.
"""
import argparse
import html
import json
import re
from pathlib import Path

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph


def extract(path):
    document = Document(path)
    title = next((p.text.strip() for p in document.paragraphs
                  if p.style.name == "Title" and p.text.strip()), Path(path).stem)
    blocks = []
    for child in document.element.body:
        if child.tag.endswith('}p'):
            p = Paragraph(child, document)
            if not p.text.strip():
                continue
            heading = re.fullmatch(r"Heading ([1-6])", p.style.name)
            blocks.append({"type": "heading" if heading else "paragraph",
                           "level": int(heading[1]) if heading else None,
                           "text": p.text})
        elif child.tag.endswith('}tbl'):
            table = Table(child, document)
            blocks.append({"type": "table", "rows": [[c.text for c in r.cells] for r in table.rows]})
    return {"title": title, "blocks": blocks}


def render(data):
    esc = html.escape
    parts = []
    for index, block in enumerate(data['blocks']):
        if index == 0 and block.get('text') == data['title']:
            parts.append('<h1>' + esc(data['title']) + '</h1>')
        elif block['type'] == 'heading':
            level = min(6, block['level'] + 1)
            parts.append(f"<h{level}>{esc(block['text'])}</h{level}>")
        elif block['type'] == 'table':
            parts.append('<table><tbody>' + ''.join('<tr>' + ''.join(
                '<td>' + esc(cell) + '</td>' for cell in row) + '</tr>'
                for row in block['rows']) + '</tbody></table>')
        else:
            parts.append('<p>' + esc(block['text']) + '</p>')
    return ('<!doctype html><html lang="en"><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>' + esc(data['title']) + '</title><style>'
            'body{margin:0;background:#eef3f2;color:#173b39;font:18px/1.6 system-ui}'
            'main{max-width:820px;margin:40px auto;background:white;padding:40px;border-radius:20px}'
            'small{letter-spacing:.12em;color:#54726e}h1,h2{line-height:1.2}'
            'table{border-collapse:collapse;width:100%}td{border:1px solid #ccdcd8;padding:12px}'
            '@media(max-width:600px){main{padding:20px;margin:12px}}</style>'
            '<main><small>VIETNAM ADVENTURE PUBLISHER / FICTIONAL DEMO</small>'
            + ''.join(parts) + '</main></html>')


def main(argv=None):
    parser = argparse.ArgumentParser(description='Extract DOCX text, headings and tables to HTML and JSON.')
    parser.add_argument('input', type=Path)
    parser.add_argument('--output-dir', type=Path, default=Path('output'))
    args = parser.parse_args(argv)
    if args.input.suffix.lower() != '.docx' or not args.input.is_file():
        parser.error('input must be an existing .docx file')
    try:
        data = extract(args.input)
    except Exception as exc:
        parser.error(f'cannot read DOCX: {exc}')
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for suffix, content in [('json', json.dumps(data, ensure_ascii=False, indent=2)), ('html', render(data))]:
        destination = args.output_dir / f'{args.input.stem}.{suffix}'
        if destination.exists():
            parser.error(f'output already exists: {destination}; choose a new output directory')
    for suffix, content in [('json', json.dumps(data, ensure_ascii=False, indent=2)), ('html', render(data))]:
        (args.output_dir / f'{args.input.stem}.{suffix}').write_text(content, encoding='utf-8')
    print(f"Published {len(data['blocks'])} blocks to {args.output_dir}")


if __name__ == '__main__':
    main()
