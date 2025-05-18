from __future__ import annotations
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from kamers import Kamer
    from woning import Woning


class Apparaten:
    def __init__(self):
        self.lijst: list[Apparaat] = []


class Apparaat:
    def __init__(self, naam, woning: Woning, kamer: Optional[Kamer] = None):
        self.naam = naam
        self.woning = woning
        self.kamer = kamer
        self.status = False

    def schakel(self):
        self.status = not self.status
        self.woning.logger.sla_op(self.log_schakel(), self.woning.klok.get_tijd())

    def log_schakel(self):
        if self.status:
            return f"{self.__class__.__name__} in {self.kamer.naam} aangezet"
        else:
            return f"{self.__class__.__name__} in {self.kamer.naam} uitgezet"
