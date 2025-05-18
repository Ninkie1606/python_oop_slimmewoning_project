from .apparaten import Apparaat


class Lamp(Apparaat):
    def __init__(self, woning, naam="Lamp", helderheid=0):
        super().__init__(naam, woning)
        self.helderheid = helderheid

    def pas_helderheid_aan(self, helderheid: int):
        self.helderheid = helderheid
