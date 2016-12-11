class Registry(object):

    def __init__(self):
        self.regforms = []

    def add_regform(self, regform):
        if regform not in self.regforms:
            self.regforms.append(regform)