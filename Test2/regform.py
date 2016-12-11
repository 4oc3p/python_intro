import datetime


class RegForm(object):

    def __init__(self, person, library):
        self._result = {}  # key = product, value = qty
        self.library = library
        self.person = person
        self.provide_date = None
        self.give_back_date = None

    def result(self):
        return self._result

    @staticmethod
    def date():
        return datetime.datetime.now().strftime("%d.%m.%y")

    def provide(self, product, qty):
        self.library.permission()[self.person] = self.library.permission().get(self.person, 0)
        if qty <= self.library.quantity(product):
            if self.library.permission().get(self.person) + qty <= 3:
                self.result()[product] = self.result().get(product, 0) + qty
                self.library.remove_product(product, qty)
                self.library.permission()[self.person] += qty
                self.provide_date = RegForm.date()
            else:
                raise BaseException('More than 3 product')
        else:
            raise ValueError('There is no such product')

    def give_back(self, product, qty):
        if qty <= self.result()[product]:
            self.library.permission()[self.person] -= qty
            self.library.add_product(product, qty)
            if qty == self.result()[product] and self.library.permission()[self.person] == 0:
                self.give_back_date = RegForm.date()
        else:
            raise ValueError('Cannot return more than taken!')


