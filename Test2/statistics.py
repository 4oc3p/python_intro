class Statistics(object):

    def __init__(self, registry):
        self.registry = registry.regforms

    def person(self):
        for regform in self.registry:
            print(regform.person.fullname)