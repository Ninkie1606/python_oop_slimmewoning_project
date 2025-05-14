from __future__ import annotations

from woning import Woning
from kamers import Kamer
from bewoners import Bewoner
from apparaten import Lamp, Thermostaat, Deur, Bewegingssensor, Rookmelder, Gordijn
import time


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
        kamer.voeg_apparaat_toe(Lamp("Lamp"))
        kamer.voeg_apparaat_toe(Thermostaat("Thermostaat"))
        kamer.voeg_apparaat_toe(Deur("Deur"))
        kamer.voeg_apparaat_toe(Bewegingssensor("Bewegingssensor"))
        kamer.voeg_apparaat_toe(Rookmelder("Rookmelder"))
        if kamer.naam not in ["gang", "badkamer", "wc"]:
            kamer.voeg_apparaat_toe(Gordijn("Gordijn"))

    while True:
        woning.klok.tik()

        for bewoner in woning.bewoners.lijst:
            bewoner.beweeg(woning.kamers.lijst)

        woning.smarthub.update()

        woning.logger.sla_op("Stap voltooid", woning.klok.get_tijd())
        woning.html_gen.gen_html()
        woning.logger.schrijf_weg()
        time.sleep(snelheid)


if __name__ == "__main__":
    main()
