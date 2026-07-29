"""
word_publisher.py

Semantic Word publisher.
"""

from __future__ import annotations

from docx import Document

from .formatter import Formatter


class WordPublisher:

    def __init__(self):

        self.formatter = Formatter()

    def publish(
        self,
        handbook,
        output_path=None,
    ):

        document = Document()

        self._publish_title(
            document,
            handbook,
        )

        self._publish_chapters(
            document,
            handbook,
        )

        if output_path:

            document.save(output_path)

        return document

    # ----------------------------------------------------------

    def _publish_title(
        self,
        document,
        handbook,
    ):

        title = getattr(
            handbook,
            "title",
            "",
        )

        if title:

            document.add_heading(
                title,
                level=0,
            )

    # ----------------------------------------------------------

    def _publish_chapters(
        self,
        document,
        handbook,
    ):

        for chapter in handbook.chapters:

            self._publish_chapter(
                document,
                chapter,
            )

    # ----------------------------------------------------------

    def _publish_chapter(
        self,
        document,
        chapter,
    ):

        heading = f"Chapter {chapter.number}"

        if chapter.title:

            heading += f" - {chapter.title}"

        document.add_heading(
            heading,
            level=1,
        )

        for component in chapter.components:

            self.formatter.render(
                document,
                component,
            )