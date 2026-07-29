"""
block_detector.py

Detects semantic blocks inside a chapter.

Current Version:
- Groups components into blocks.
- Starts a new block whenever a component marked as a section
  heading is encountered.
- If no section headings exist, the entire chapter becomes one block.

Future versions may add configurable rules.
"""

from vap.models.block import Block


class BlockDetector:
    """
    Detect semantic blocks from chapter components.
    """

    def detect(self, chapter):
        """
        Returns a list of Block objects.
        """

        blocks = []

        current_block = Block(
            title=chapter.title,
            block_type="chapter"
        )

        for component in chapter.components:

            is_section = getattr(component, "component_type", "") == "section"

            if is_section and current_block.component_count > 0:

                blocks.append(current_block)

                current_block = Block(
                    title=getattr(component, "title", ""),
                    block_type="section"
                )

            current_block.add_component(component)

        if current_block.component_count > 0:
            blocks.append(current_block)

        return blocks