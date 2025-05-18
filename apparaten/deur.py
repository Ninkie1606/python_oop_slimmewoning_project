from .apparaten import Apparaat


class Deur(Apparaat):
    def __init__(self, woning, naam="Deur"):
        super().__init__(naam, woning)
        self.isopen = False

    def ontgrendel(self):
        self.isopen = True

    def vergrendel(self):
        self.isopen = False
