from .apparaten import Apparaat
from datetime import datetime, timedelta


class Klok(Apparaat):
    def __init__(self, woning, starttijd="06:00", stap_grootte_in_minuten=10):
        super().__init__("Klok", woning)
        self.tijd_per_stap = timedelta(minutes=stap_grootte_in_minuten)
        self.huidige_tijd = datetime.strptime(starttijd, "%H:%M").replace(
            year=2025, month=1, day=1
        )

    def tik(self):
        self.huidige_tijd += self.tijd_per_stap

    def get_tijd(self):
        return self.huidige_tijd

    def get_tijd_str(self):
        return self.huidige_tijd.strftime("%H:%M")
