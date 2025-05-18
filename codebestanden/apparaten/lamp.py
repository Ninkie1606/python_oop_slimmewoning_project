from .apparaten import Apparaat


class Lamp(Apparaat):
    def __init__(self, woning, kamer, naam="Lamp", helderheid=0):
        super().__init__(naam, woning, kamer)
        self.helderheid = helderheid

    def pas_helderheid_aan(self, helderheid: int):
        self.helderheid = helderheid
        self.woning.logger.sla_op(self.log_helderheid(), self.woning.klok.get_tijd())

    def log_helderheid(self):
        return f"lamp in {self.kamer.naam} aangepast naar {self.helderheid}% helderheid"
