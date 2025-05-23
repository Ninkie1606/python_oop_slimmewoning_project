from __future__ import annotations
from typing import TYPE_CHECKING
import random

if TYPE_CHECKING:
    from kamers import Kamer
    from woning import Woning


class Bewoners:
    def __init__(self):
        self.lijst: list[Bewoner] = []


class Bewoner:
    def __init__(self, naam, woning):
        self.naam = naam
        self.huidige_kamer: Kamer = None
        self.woning: Woning = woning

    def beweeg(self, kamerlijst: list[Kamer]):
        if self.huidige_kamer is not None:
            self.huidige_kamer.huidige_bewoners.lijst.remove(self)

        nieuwe_kamer = random.choice(kamerlijst)
        self.huidige_kamer = nieuwe_kamer

        nieuwe_kamer.huidige_bewoners.lijst.append(self)

        # bewoner en welke kamer data opslaan
        self.woning.ai.data_maken({"bewoner": self.naam, "kamer": nieuwe_kamer.naam})

    def slaap(self, kamerlijst: list[Kamer]):
        if self.huidige_kamer is not None:
            self.huidige_kamer.huidige_bewoners.lijst.remove(self)

        nieuwe_kamer = "slaapkamer2" if self.naam == "nick" else "slaapkamer1"

        for kamer in kamerlijst:
            if kamer.naam == nieuwe_kamer:
                kamer.huidige_bewoners.lijst.append(self)
                self.huidige_kamer = kamer
