"""
base_renderer.py

Base class for all semantic renderers.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from vap.publishing.theme import Theme


class BaseRenderer(ABC):

    def __init__(self):

        self.theme = Theme()

    @abstractmethod
    def render(
        self,
        document,
        component,
    ):
        raise NotImplementedError