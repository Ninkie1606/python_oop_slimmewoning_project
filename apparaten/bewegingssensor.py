from __future__ import annotations
from .apparaten import Apparaat
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from kamers import Kamer


class Bewegingssensor(Apparaat):
    def __init__(self, woning, kamer: Kamer, naam="Bewegingssensor"):
        super().__init__(naam, woning)
        self.isbeweging = False
        self.kamer = kamer

    def detecteer_beweging(self):
        if len(self.kamer.huidige_bewoners.lijst) >= 1:
            self.isbeweging = True
            self.woning.logger.sla_op(
                self.log_bewegingssensor(), self.woning.klok.get_tijd()
            )
        else:
            self.isbeweging = False

    def log_bewegingssensor(self):
        if self.isbeweging:
            return f"bewegingssensor in {self.kamer.naam} ziet activiteit"
