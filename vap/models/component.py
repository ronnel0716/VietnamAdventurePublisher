from dataclasses import dataclass, field

from .enums import ComponentType


@dataclass
class Component:
    component_type: ComponentType = ComponentType.UNKNOWN

    heading: str = ""

    paragraphs: list[str] = field(default_factory=list)

    table_index: int | None = None

    image_index: int | None = None

    style_name: str = ""

    start_index: int = 0

    end_index: int = 0