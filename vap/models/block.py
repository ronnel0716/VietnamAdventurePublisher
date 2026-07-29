"""
block.py

Represents a semantic block inside a chapter.

A block groups one or more related components.

Example:

Chapter
 ├── Hero Block
 ├── Travel Information Block
 ├── Food Block
 └── QR Directory Block
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .component import Component


@dataclass(slots=True)
class Block:
    """
    A semantic block within a chapter.
    """

    title: str = ""

    block_type: str = "generic"

    components: list[Component] = field(default_factory=list)

    start_index: int = 0

    end_index: int = 0

    def add_component(self, component: Component) -> None:
        """
        Adds a component to this block.
        """
        self.components.append(component)

    @property
    def component_count(self) -> int:
        return len(self.components)

    def is_empty(self) -> bool:
        return self.component_count == 0

    def __len__(self) -> int:
        return self.component_count

    def __iter__(self):
        return iter(self.components)

    def __str__(self) -> str:
        return (
            f"Block("
            f"type='{self.block_type}', "
            f"title='{self.title}', "
            f"components={self.component_count})"
        )