from vap.models.enums import ComponentType
from vap.semantic.base_rule import SemanticRule


class HeadingRule(SemanticRule):

    def matches(self, paragraph):

        return paragraph.style.startswith("Heading")

    def component_type(self):

        return ComponentType.HEADING