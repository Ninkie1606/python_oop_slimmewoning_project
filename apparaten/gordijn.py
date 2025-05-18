from .apparaten import Apparaat


class Gordijn(Apparaat):
    def __init__(self, woning, naam="Gordijn"):
        super().__init__(naam, woning)
        self.isopen = False

    def openen(self):
        self.isopen = True

    def sluiten(self):
        self.isopen = False
