from .apparaten import Apparaat


class Deur(Apparaat):
    def __init__(self, woning, kamer, naam="Deur"):
        super().__init__(naam, woning, kamer)
        self.isopen = False

    def ontgrendel(self):
        self.isopen = True

    def vergrendel(self):
        self.isopen = False
        self.woning.logger.sla_op(self.log_deur(), self.woning.klok.get_tijd())

    def log_deur(self):
        if self.isopen:
            return f"deur in {self.kamer.naam} geopend"
        else:
            return f"deur in {self.kamer.naam} gesloten"
