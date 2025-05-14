from __future__ import annotations
from datetime import datetime, timedelta
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from kamers import Kamer


class Apparaten:
    def __init__(self):
        self.lijst: list[Apparaat] = []


class Apparaat:
    def __init__(self, naam: str = ""):
        self.naam = naam
        self.status = False

    def schakel(self):
        self.status = not self.status


class Lamp(Apparaat):
    def __init__(self, naam="Lamp", helderheid=60):
        super().__init__(naam)
        self.helderheid = helderheid

    def pas_helderheid_aan(self, helderheid: int):
        self.helderheid = helderheid


class Thermostaat(Apparaat):
    def __init__(self, naam="Thermostaat"):
        super().__init__(naam)
        self.temperatuur = 20

    def pas_temperatuur_aan(self, temp: int):
        self.temperatuur = temp


class Deurslot(Apparaat):
    def __init__(self, naam="Deurslot"):
        super().__init__(naam)

    def ontgrendel(self):
        self.status = False

    def vergrendel(self):
        self.status = True


class Bewegingssensor(Apparaat):
    def __init__(self, naam="Bewegingssensor"):
        super().__init__(naam)
        self.isbeweging = False

    def detecteer_beweging(self, kamer: Kamer):
        return len(kamer.huidige_bewoners.lijst) >= 1


class Rookmelder(Apparaat):
    def __init__(self, naam="Rookmelder"):
        super().__init__(naam)
        self.isrook = False

    def activeer_alarm(self):
        self.isrook = True

    def deactiveer_alarm(self):
        self.isrook = False


class Gordijn(Apparaat):
    def __init__(self, naam="Gordijn"):
        super().__init__(naam)
        self.isopen = False

    def openen(self):
        self.isopen = True

    def sluiten(self):
        self.isopen = False


class Klok(Apparaat):
    def __init__(self, starttijd="06:00", stap_grootte_in_minuten=10):
        super().__init__("Klok")
        self.tijd_per_stap = timedelta(minutes=stap_grootte_in_minuten)
        self.huidige_tijd = datetime.strptime(starttijd, "%H:%M")

    def tik(self):
        self.huidige_tijd += self.tijd_per_stap

    def get_tijd(self):
        return self.huidige_tijd

    def get_tijd_str(self):
        return self.huidige_tijd.strftime("%H:%M")
