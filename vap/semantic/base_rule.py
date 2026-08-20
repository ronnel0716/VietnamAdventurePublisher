from abc import ABC, abstractmethod


class SemanticRule(ABC):

    @abstractmethod
    def matches(self, paragraph):

        raise NotImplementedError

    @abstractmethod
    def component_type(self):

        raise NotImplementedError