from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from woning import Woning


class Apparaten:
    def __init__(self):
        self.lijst: list[Apparaat] = []


class Apparaat:
    def __init__(self, naam, woning: Woning):
        self.naam = naam
        self.woning = woning
        self.status = False

    def schakel(self):
        self.status = not self.status
