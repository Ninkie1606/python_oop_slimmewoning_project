from .apparaten import Apparaat


class Rookmelder(Apparaat):
    def __init__(self, woning, kamer, naam="Rookmelder"):
        super().__init__(naam, woning, kamer)
        self.isrook = False

    def activeer_alarm(self):
        self.isrook = True
        self.woning.logger.sla_op(self.log_rookmelder(), self.woning.klok.get_tijd())

    def deactiveer_alarm(self):
        self.isrook = False
        self.woning.logger.sla_op(self.log_rookmelder(), self.woning.klok.get_tijd())

    def log_rookmelder(self):
        if self.isrook:
            return f"rookmelder in {self.kamer.naam} geactiveerd"
        else:
            return f"gordijn in {self.kamer.naam} gedeactiveerd"
