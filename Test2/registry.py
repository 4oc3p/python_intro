class Registry(object):

    def __init__(self):
        self.regforms = []

    def add_regfrom(self, regform):
        if regform not in self.regforms:
            self.regforms.append(regform)