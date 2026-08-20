from vap.semantic.rules.heading_rule import HeadingRule
from vap.semantic.rules.paragraph_rule import ParagraphRule


class SemanticClassifier:

    def __init__(self):

        self.rules = [

            HeadingRule(),

            ParagraphRule(),   # fallback

        ]

    def classify(self, paragraph):

        for rule in self.rules:

            if rule.matches(paragraph):

                return rule.component_type()