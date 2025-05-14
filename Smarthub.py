from __future__ import annotations
from typing import TYPE_CHECKING
from apparaten import Thermostaat, Deur, Lamp, Gordijn, Bewegingssensor

if TYPE_CHECKING:
    from woning import Woning


class Smarthub:
    def __init__(self, woning: Woning):
        self.woning: Woning = woning

    def update(self):
        # check welke tijd het is

        hour = self.woning.klok.huidige_tijd.hour
        if 6 <= hour and hour < 22:  # dag
            print("dag")
            for kamer in self.woning.kamers.lijst:
                for apparaat in kamer.apparaten.lijst:
                    if isinstance(apparaat, Thermostaat):  # dag termostaat
                        if apparaat.status == False:  # als uit staat zet aan
                            apparaat.schakel()
                            apparaat.pas_temperatuur_aan(22)
                    if (
                        isinstance(apparaat, Deur) and not kamer.naam == "gang"
                    ):  # gang moet toe blijven (voordeur)
                        apparaat.ontgrendel()
                    if isinstance(apparaat, Lamp):
                        apparaat.pas_helderheid_aan(0)
                    if isinstance(apparaat, Gordijn):
                        apparaat.openen()

        elif hour < 6 or hour >= 22:  # nacht
            print("nacht")
            for kamer in self.woning.kamers.lijst:
                for apparaat in kamer.apparaten.lijst:  # alle apparaten
                    if isinstance(apparaat, Thermostaat):  # nacht thermostaat
                        if apparaat.status == True:  # als aan staat zet uit
                            apparaat.pas_temperatuur_aan(16)
                            apparaat.schakel()
                    if isinstance(apparaat, Deur):
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
