from kamers import Kamers, Kamer
from bewoners import Bewoners, Bewoner
from smarthub import Smarthub
from apparaten import (
    Klok,
    Lamp,
    Thermostaat,
    Deurslot,
    Bewegingssensor,
    Rookmelder,
    Gordijn,
)
from logger import Logger
from htmlgen import HTMLGen


class Woning:
    def __init__(self, naam):
        self.naam = naam
        self.Kamers: Kamers = Kamers()
        self.bewoners: Bewoners = Bewoners()
        self.smarthub = Smarthub(self)
        self.klok = Klok()
        self.logger = Logger()
        self.html_gen = HTMLGen()

    def voeg_kamer_toe(self, kamer: Kamer):
        self.Kamers.lijst.append(kamer)

    def voeg_bewoner_toe(self, bewoner: Bewoner):
        self.bewoners.lijst.append(bewoner)

    def start_simulatie(self):
        self.voeg_kamer_toe(Kamer("keuken"))
        self.voeg_kamer_toe(Kamer("living"))
        self.voeg_kamer_toe(Kamer("slaapkamer1"))
        self.voeg_kamer_toe(Kamer("slaapkamer2"))
        self.voeg_kamer_toe(Kamer("wc"))
        self.voeg_kamer_toe(Kamer("badkamer"))
        self.voeg_kamer_toe(Kamer("gang"))
        self.voeg_bewoner_toe(Bewoner("mama"))
        self.voeg_bewoner_toe(Bewoner("papa"))
        self.voeg_bewoner_toe(Bewoner("zusje"))
        self.voeg_bewoner_toe(Bewoner("nick"))

        for kamer in self.Kamers.lijst:
            kamer.voeg_apparaat_toe(Lamp("Lamp"))
            kamer.voeg_apparaat_toe(Thermostaat("Thermostaat"))
            kamer.voeg_apparaat_toe(Deurslot("Deurslot"))
            kamer.voeg_apparaat_toe(Bewegingssensor("Bewegingssensor"))
            kamer.voeg_apparaat_toe(Rookmelder("Rookmelder"))
            if kamer.naam not in ["gang", "badkamer", "wc"]:
                kamer.voeg_apparaat_toe(Gordijn("Gordijn"))

        for bewoner in self.bewoners.lijst:
            bewoner.beweeg(self.Kamers.lijst)
