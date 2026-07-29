"""TODO: Foundation Pack implementation."""
from dataclasses import dataclass, field

from .component import Component


@dataclass
class Chapter:
    """
    Represents one handbook chapter.
    """

    number: int

    title: str = ""

    start_index: int = 0

    end_index: int = 0

    components: list[Component] = field(default_factory=list)

    def add_component(self, component: Component):
        self.components.append(component)

    @property
    def component_count(self):
        return len(self.components)

    def __len__(self):
        return len(self.components)

    def __iter__(self):
        return iter(self.components)