from bewoners import Bewoners, Bewoner
from datetime import datetime, timedelta
from logger import Logger
from kamers import Kamer

class Apparaten:
    def __init__(self):
        self.lijst: list[Apparaat] = []


class Apparaat:
    def __init__(
        self,
        naam
    ):
        self.naam = naam
        self.status = False

    def schakel(self):
        if self.status:
            self.status = False
        else:
            self.status = True


class Lamp(Apparaat):
    def __init__(self, helderheid=60):
        super().__init__()
        self.helderheid = helderheid

    def pas_helderheid_aan(self, helderheid):
        self.helderheid = helderheid


class Thermostaat(Apparaat):
    def __init__(self):
        super().__init__()
        self.temperatuur = 20

    def pas_temperatuur_aan(self, temp):  # moet temperatuur van woning aanpassen
        self.temperatuur = temp


class Deurslot(Apparaat):
    def __init__(self):
        super().__init__()

    def ontgrendel(self):
        self.status = False

    def vergrendel(self):
        self.status = True


class Bewegingssensor(Apparaat):
    def __init__(self):
        super().__init__()
        self.isbeweging = False

    def detecteer_beweging(self,kamer:Kamer):  # detecteert beweging in kamer
        if kamer.huidige_bewoners >= 1:
            return True
        else:
            return False


class Rookmelder(Apparaat):
    def __init__(self):
        super().__init__()
        self.isrook = False

    def activeer_alarm(self):
        self.isrook = True

    def deactiveer_alarm(self):
        self.isrook = False


class Gordijn(Apparaat):
    def __init__(self):
        super().__init__()
        self.isopen = False

    def openen(self):
        self.isopen = True

    def sluiten(self):
        self.isopen = False


class Klok(Apparaat):
    def __init__(self, starttijd="06:00", stap_grootte_in_minuten=10):
        super().__init__()
        self.tijd_per_stap = timedelta(minutes=stap_grootte_in_minuten)
        self.huidige_tijd = datetime.strptime(starttijd, "%H:%M")

    def tik(self):  # 1 stap
        self.huidige_tijd += self.tijd_per_stap

    def get_tijd(self):
        return self.huidige_tijd

    def get_tijd_str(self):
        return self.huidige_tijd.strftime("%H:%M")