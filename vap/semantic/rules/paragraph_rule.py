from vap.models.enums import ComponentType
from vap.semantic.base_rule import SemanticRule


class ParagraphRule(SemanticRule):

    def matches(self, paragraph):

        return True

    def component_type(self):

        return ComponentType.PARAGRAPH