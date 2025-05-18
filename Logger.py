class Logger:
    def __init__(self):
        self.opslag: list[str] = []  # voor alle dingen per toer
        self.bestandsnaam = "Logs.txt"

    def sla_op(self, text, tijd):  # naar oplag
        self.opslag.append(f"{tijd}: {text}")

    def schrijf_weg(self):  # naar bestand
        with open(self.bestandsnaam, "a") as f:
            for regel in self.opslag:
                f.write(f"{regel} \n")
