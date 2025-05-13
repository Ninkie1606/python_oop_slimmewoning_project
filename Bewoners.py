import random
from kamers import Kamer


class Bewoners:
    def __init__(self):
        self.lijst: list[Bewoner] = []


class Bewoner:
    def __init__(self, naam):
        self.naam = naam
        self.huidige_kamer: Kamer = None

    def beweeg(self, kamerlijst: list[Kamer]):
        if self.huidige_kamer is not None:
            self.huidige_kamer.huidige_bewoners.lijst.remove(self)

        nieuwe_kamer = random.choice(kamerlijst)
        self.huidige_kamer = nieuwe_kamer

        nieuwe_kamer.huidige_bewoners.lijst.append(self)
