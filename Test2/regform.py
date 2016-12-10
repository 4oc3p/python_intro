class RegForm(object):

    def __init__(self, person, library):
        self._result = {}
        self.library = library
        self.person = person

    def result(self):
        return self._result

    def provide(self, product, qty):
        if qty <= self.library.quantity(product):
            self.result()[product] = self.result().get(product, 0) + qty
            self.library.content()[product] -= qty
        else:
            raise ValueError('There is no such product')
