from .apparaten import Apparaat


class Rookmelder(Apparaat):
    def __init__(self, woning, naam="Rookmelder"):
        super().__init__(naam, woning)
        self.isrook = False

    def activeer_alarm(self):
        self.isrook = True

    def deactiveer_alarm(self):
        self.isrook = False
