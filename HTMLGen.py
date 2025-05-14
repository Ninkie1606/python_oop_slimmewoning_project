from jinja2 import Environment, FileSystemLoader


class HTMLGen:
    def __init__(self, woning):
        self.woning = woning
        self.env = Environment(loader=FileSystemLoader("templates"))

    def gen_html(self, bestandsnaam="browser/slimme_woning.html"):
        template = self.env.get_template("huis.jinja")
        output = template.render(woning=self.woning)

        with open(bestandsnaam, "w") as f:
            f.write(output)
