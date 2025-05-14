from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from woning import Woning
    from apparaten import Thermostaat, Deurslot, Lamp, Gordijn, Bewegingssensor


class Smarthub:
    def __init__(self, woning: Woning):
        self.woning: Woning = woning

    def update(self):
        # check welke tijd het is
        if 6 <= self.woning.klok.huidige_tijd.hour <= 22:  # dag
            for kamer in self.woning.kamers.lijst:
                for apparaat in kamer.apparaten.lijst:

                    if isinstance(apparaat, Thermostaat):
                        apparaat.pas_temperatuur_aan(22)
                    if (
                        isinstance(apparaat, Deurslot) and not kamer.naam == "gang"
                    ):  # gang moet toe blijven (voordeur)
                        apparaat.ontgrendel()
                    if isinstance(apparaat, Lamp):
                        apparaat.pas_helderheid_aan(0)
                    if isinstance(apparaat, Gordijn):
                        apparaat.openen()

        if 6 >= self.woning.klok.huidige_tijd.hour >= 22:  # nacht
            for kamer in self.woning.kamers.lijst:
                for apparaat in kamer.apparaten.lijst:  # alle apparaten

                    if isinstance(apparaat, Thermostaat):
                        apparaat.pas_temperatuur_aan(16)
                    if isinstance(apparaat, Deurslot):
                        apparaat.vergrendel()
                    if isinstance(apparaat, Gordijn):
                        apparaat.sluiten()

        for kamer in self.woning.kamers.lijst:  # kamers waar mensen in zitten
            for apparaat in kamer.apparaten.lijst:
                if isinstance(apparaat, Bewegingssensor):
                    if apparaat.isbeweging:
                        for appar in kamer.apparaten.lijst:
                            if isinstance(appar, Lamp):
                                appar.pas_helderheid_aan(80)
                    else:
                        for appar in kamer.apparaten.lijst:
                            if isinstance(appar, Lamp):
                                appar.pas_helderheid_aan(0)
