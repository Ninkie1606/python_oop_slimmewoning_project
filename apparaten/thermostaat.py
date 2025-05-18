from .apparaten import Apparaat


class Thermostaat(Apparaat):
    def __init__(self, woning, naam="Thermostaat"):
        super().__init__(naam, woning)
        self.temperatuur = 20

    def pas_temperatuur_aan(self, temp: int):
        self.temperatuur = temp
