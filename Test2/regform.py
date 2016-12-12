import datetime


class RegForm(object):

    MAXIMUM_BOOKS_ON_HAND = 3

    def __init__(self, person, library):
        self._result = {}  # key = product, value = qty
        self._temp = {}
        self.library = library
        self.person = person
        self.provide_date = None
        self.give_back_date = None
        self.opened = False

    def result(self):
        return self._result

    def temp(self):
        return self._temp

    @staticmethod
    def date():
        return datetime.datetime.now().strftime("%d.%m.%y")

    def provide(self, product, qty):
        self.library.permission()[self.person] = self.library.permission().get(self.person, 0)
        if qty <= self.library.quantity(product):
            if self.library.permission().get(self.person) + qty <= RegForm.MAXIMUM_BOOKS_ON_HAND:
                self.result()[product] = self.result().get(product, 0) + qty
                self.temp[product] = self.temp.get(product, 0) + qty
                self.library.remove_product(product, qty)
                self.library.permission()[self.person] += qty
                self.provide_date = RegForm.date()
                self.opened = True
            else:
                raise BaseException('More than 3 product')
        else:
            raise ValueError('There is no such product')

    def give_back(self, product, qty):
        if qty <= self.temp[product]:
            self.library.permission()[self.person] -= qty
            self.library.add_product(product, qty)
            self.temp[product] -= qty
        else:
            raise ValueError('Cannot return more than taken!')

    def close_reg(self):
        if sum(self.temp.values()) == 0:
            self.give_back_date = RegForm.date()
            self.opened = False
        else:
            print("Not all products have returned")


