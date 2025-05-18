from .apparaten import Apparaat


class Gordijn(Apparaat):
    def __init__(self, woning, kamer, naam="Gordijn"):
        super().__init__(naam, woning, kamer)
        self.isopen = False

    def openen(self):
        self.isopen = True
        self.woning.logger.sla_op(self.log_gordijn(), self.woning.klok.get_tijd())

    def sluiten(self):
        self.isopen = False
        self.woning.logger.sla_op(self.log_gordijn(), self.woning.klok.get_tijd())

    def log_gordijn(self):
        if self.isopen:
            return f"gordijn in {self.kamer.naam} geopend"
        else:
            return f"gordijn in {self.kamer.naam} gesloten"
