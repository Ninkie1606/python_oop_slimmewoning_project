from .apparaten import Apparaat
from datetime import datetime, timedelta


class Klok(Apparaat):
    def __init__(self, woning, starttijd="06:00", stap_grootte_in_minuten=10):
        super().__init__("Klok", woning)
        self.tijd_per_stap = timedelta(minutes=stap_grootte_in_minuten)
        self.huidige_tijd = datetime.strptime(starttijd, "%H:%M")

    def tik(self):
        self.huidige_tijd += self.tijd_per_stap

    def get_tijd(self):
        return self.huidige_tijd

    def get_tijd_str(self):
        return self.huidige_tijd.strftime("%H:%M")

    def log(self):
        pass
