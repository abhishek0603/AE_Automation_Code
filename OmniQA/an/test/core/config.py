import configparser

class Config():
    def __init__(self, filename="tests.cfg",filename1="AudBuilder.cfg"):
        parser = configparser.ConfigParser()
        parser.read(filename)
        self.config = dict(parser.items("DEFAULT"))
        for section in parser.sections():
            self.config[section] = dict(parser.items(section))

        parser_ab = configparser.ConfigParser()
        parser_ab.read(filename1)
        self.configAB = dict(parser_ab)
        for section_ab in parser_ab.sections():
            self.configAB[section_ab] = dict(parser_ab.items(section_ab))

    def get_config(self):
        return self.config

    def get_config_ab(self):
        return self.configAB
