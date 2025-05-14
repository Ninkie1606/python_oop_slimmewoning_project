from __future__ import annotations
from apparaten import Klok
from logger import Logger
from htmlgen import HTMLGen
from kamers import Kamer, Kamers
from bewoners import Bewoner, Bewoners
from smarthub import Smarthub


class Woning:
    def __init__(self, naam: str):
        self.naam = naam
        self.kamers: Kamers = Kamers()
        self.bewoners: Bewoners = Bewoners()
        self.smarthub = Smarthub(self)
        self.klok = Klok()
        self.logger = Logger()
        self.html_gen = HTMLGen(self)

    def voeg_kamer_toe(self, kamer: Kamer):
        self.kamers.lijst.append(kamer)

    def voeg_bewoner_toe(self, bewoner: Bewoner):
        self.bewoners.lijst.append(bewoner)
