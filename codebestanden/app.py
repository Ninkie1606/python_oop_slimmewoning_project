from __future__ import annotations

from woning import Woning
from kamers import Kamer
from bewoners import Bewoner
from apparaten import (
    Bewegingssensor,
    Deur,
    Gordijn,
    Lamp,
    Rookmelder,
    Thermostaat,
    Klok,
)
import time
import random


def main():
    snelheid = int(
        input(f"voer hier de aantal seconden per stap in. (snelheid van het programma)")
    )

    woning = Woning("Huis Van Nick")

    woning.voeg_kamer_toe(Kamer("keuken"))
    woning.voeg_kamer_toe(Kamer("living"))
    woning.voeg_kamer_toe(Kamer("slaapkamer1"))
    woning.voeg_kamer_toe(Kamer("slaapkamer2"))
    woning.voeg_kamer_toe(Kamer("wc"))
    woning.voeg_kamer_toe(Kamer("badkamer"))
    woning.voeg_kamer_toe(Kamer("gang"))
    woning.voeg_bewoner_toe(Bewoner("mama"))
    woning.voeg_bewoner_toe(Bewoner("papa"))
    woning.voeg_bewoner_toe(Bewoner("zusje"))
    woning.voeg_bewoner_toe(Bewoner("nick"))

    for kamer in woning.kamers.lijst:
        kamer.voeg_apparaat_toe(Lamp(woning, kamer, "Lamp"))
        kamer.voeg_apparaat_toe(Thermostaat(woning, kamer, "Thermostaat"))
        kamer.voeg_apparaat_toe(Deur(woning, kamer, "Deur"))
        kamer.voeg_apparaat_toe(Bewegingssensor(woning, kamer, "Bewegingssensor"))
        kamer.voeg_apparaat_toe(Rookmelder(woning, kamer, "Rookmelder"))
        if kamer.naam not in ["gang", "badkamer", "wc"]:
            kamer.voeg_apparaat_toe(Gordijn(woning, kamer, "Gordijn"))

    nacht_ingegaan = False
    while True:
        woning.klok.tik()
        hour = woning.klok.huidige_tijd.hour

        if 6 <= hour and hour < 22:  # dag
            nacht_ingegaan = False
            for bewoner in woning.bewoners.lijst:
                bewoner.beweeg(woning.kamers.lijst)

        else:  # nacht
            if not nacht_ingegaan:
                for bewoner in woning.bewoners.lijst:
                    bewoner.slaap(woning.kamers.lijst)
                nacht_ingegaan = True

        # brand
        for kamer in woning.kamers.lijst:
            for apparaat in kamer.apparaten.lijst:
                if isinstance(apparaat, Rookmelder) and not apparaat.status:
                    apparaat.schakel()
                if isinstance(apparaat, Rookmelder):
                    is_rook = random.randint(1, 10000)

                    if is_rook == 5:  # brand
                        apparaat.activeer_alarm()
                        # alle bewoners vluchten
                        woning.bewoners.lijst.clear()

                        for kamer in woning.kamers.lijst:
                            kamer.huidige_bewoners.lijst.clear()
                        apparaat.woning.logger.sla_op(
                            "bewoners hebben de woning verlaten", woning.klok.get_tijd()
                        )
                        # alle apparaten uit
                        for kamer in woning.kamers.lijst:
                            for apparaat in kamer.apparaten.lijst:
                                apparaat.status = False
                                apparaat.woning.logger.sla_op(
                                    apparaat.log_schakel(), woning.klok.get_tijd()
                                )

                        woning.logger.sla_op(
                            "evacuatie voltooid", woning.klok.get_tijd()
                        )
                        woning.html_gen.gen_html()
                        exit()

        woning.smarthub.update()
        woning.logger.sla_op("Stap voltooid", woning.klok.get_tijd())
        woning.html_gen.gen_html()
        time.sleep(snelheid)


if __name__ == "__main__":
    main()
