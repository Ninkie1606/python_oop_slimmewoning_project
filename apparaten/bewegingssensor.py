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
            if self.status == False:
                self.schakel()
        else:
            self.isbeweging = False
            if self.status == True:
                self.schakel()
