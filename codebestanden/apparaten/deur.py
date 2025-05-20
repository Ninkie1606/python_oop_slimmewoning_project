from .apparaten import Apparaat


class Deur(Apparaat):
    def __init__(self, woning, kamer, naam="Deur"):
        super().__init__(naam, woning, kamer)
        self.is_open = False

    def ontgrendel(self):
        self.is_open = True

    def vergrendel(self):
        self.is_open = False
        self.woning.logger.sla_op(self.log_deur(), self.woning.klok.get_tijd())

    def log_deur(self):
        if self.is_open:
            return f"deur in {self.kamer.naam} geopend"
        else:
            return f"deur in {self.kamer.naam} gesloten"
