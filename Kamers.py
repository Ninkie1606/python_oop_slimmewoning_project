from __future__ import annotations
from typing import TYPE_CHECKING
from apparaten import Apparaat, Apparaten
from bewoners import Bewoners


class Kamers:
    def __init__(self):
        self.lijst: list[Kamer] = []


class Kamer:
    def __init__(self, naam: str):
        self.naam = naam
        self.apparaten = Apparaten()
        self.huidige_bewoners = Bewoners()

    def voeg_apparaat_toe(self, apparaat: Apparaat):
        self.apparaten.lijst.append(apparaat)
