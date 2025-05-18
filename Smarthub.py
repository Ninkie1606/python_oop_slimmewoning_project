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

            # checken of bewoners bewegen
            for (
                kamer
            ) in (
                self.woning.kamers.lijst
            ):  # alle bewegingsensors beweging laten detecten
                for apparaat in kamer.apparaten.lijst:
                    if isinstance(apparaat, Bewegingssensor):
                        apparaat.detecteer_beweging()

            for kamer in self.woning.kamers.lijst:
                for apparaat in kamer.apparaten.lijst:
                    if isinstance(apparaat, Bewegingssensor) and apparaat.isbeweging:
                        for appar in kamer.apparaten.lijst:
                            if isinstance(appar, Lamp):
                                if not appar.status:
                                    appar.schakel()
                                    appar.pas_helderheid_aan(80)
                    elif (
                        isinstance(apparaat, Bewegingssensor)
                        and not apparaat.isbeweging
                    ):
                        for appar in kamer.apparaten.lijst:
                            if isinstance(appar, Lamp):
                                if appar.status:
                                    appar.schakel()
                                    appar.pas_helderheid_aan(0)

            # dag gerelateerd zonder positie bewoners
            for kamer in self.woning.kamers.lijst:
                for apparaat in kamer.apparaten.lijst:
                    if isinstance(apparaat, Thermostaat):  # dag termostaat
                        if not apparaat.status:  # als uit staat zet aan
                            apparaat.schakel()
                            apparaat.pas_temperatuur_aan(22)

                    if (
                        isinstance(apparaat, Deur) and not kamer.naam == "gang"
                    ):  # gang moet toe blijven (voordeur)
                        if not apparaat.isopen:  # als niet open is
                            apparaat.ontgrendel()
                            apparaat.schakel()

                    if isinstance(apparaat, Gordijn):
                        if not apparaat.status:
                            apparaat.schakel()
                            apparaat.openen()

        else:  # nacht
            print("nacht")

            # checken of bewoners bewegen
            for (
                kamer
            ) in (
                self.woning.kamers.lijst
            ):  # alle bewegingsensors beweging laten detecten
                for apparaat in kamer.apparaten.lijst:
                    if isinstance(apparaat, Bewegingssensor):
                        apparaat.detecteer_beweging()

            for kamer in self.woning.kamers.lijst:
                for apparaat in kamer.apparaten.lijst:  # alle apparaten
                    if isinstance(apparaat, Thermostaat):  # nacht thermostaat
                        if apparaat.status:  # als aan staat zet uit
                            apparaat.pas_temperatuur_aan(16)
                            apparaat.schakel()
                    if isinstance(apparaat, Deur):  # als nacht deur moet toe
                        if apparaat.isopen:
                            apparaat.vergrendel()
                            apparaat.schakel()
                    if isinstance(apparaat, Gordijn):
                        if apparaat.status:
                            apparaat.schakel()
                            apparaat.sluiten()
