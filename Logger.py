class Logger:
    def __init__(self):
        self.bestandsnaam = "Logs.txt"

    def sla_op(self, text, tijd):
        with open(self.bestandsnaam, "a") as f:
            f.write(f"{tijd}: {text}\n")
