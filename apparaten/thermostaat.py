from .apparaten import Apparaat


class Thermostaat(Apparaat):
    def __init__(self, woning, kamer, naam="Thermostaat"):
        super().__init__(naam, woning, kamer)
        self.temperatuur = 22

    def pas_temperatuur_aan(self, temp: int):
        self.temperatuur = temp
        self.woning.logger.sla_op(self.log_temperatuur(), self.woning.klok.get_tijd())

    def log_temperatuur(self):
        return (
            f"temperatuur in {self.kamer.naam} aangepast naar {self.temperatuur} graden"
        )
