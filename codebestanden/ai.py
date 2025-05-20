import json
import os


class Ai:
    """krijgt data binnen van apparaten die data in een file stoppen"""

    def __init__(self):
        self.bestandsnaam = "data.json"
        self.data = {}

    def data_maken(self, data):
        if os.path.exists(self.bestandsnaam):  # als file bestaat
            with open(self.bestandsnaam, "r") as f:  # lees bestand
                try:  # neem data over als er in zit
                    bestaande_data = json.load(f)
                except:
                    bestaande_data = []
        else:
            bestaande_data = []

        bestaande_data.append(data)

        with open(self.bestandsnaam, "w") as f:
            json.dump(bestaande_data, f)

    def data_ophalen(self):  # per dag data ophalen
        pass

    def data_verwerken():  # per dag iets met de data doen
        pass
