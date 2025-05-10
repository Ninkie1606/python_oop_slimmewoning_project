from Apparaten import Apparaten, Apparaat
from Bewoners import Bewoners, Bewoner


class Kamers:
    def __init__(self):
        self.lijst: list[Kamer] = []


class Kamer:
    def __init__(self, naam):
        self.naam = naam
        self.apparaten = Apparaten()
        self.huidige_bewoners = Bewoners()

    def voeg_apparaat_toe(self, apparaat: Apparaat):
        self.apparaten.lijst.append(apparaat)
