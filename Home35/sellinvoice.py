from time import asctime
from time import localtime as l
from Home35 import store


class SellInvoice:

    id = 0

    def __init__(self, item, quantity, store, user_discount=0):
        self.item_name = item.name
        self._quantity = None
        self.quantity = quantity
        self.shelf_price = item.shelf_price
        self.store = store
        self.user_discount = user_discount
        self.sum = 0
        self.date = asctime()
        SellInvoice.id += 1
        self.id = "%d/%d/%d/%d" % (SellInvoice.id, l()[2], l()[1], l()[0] % 100)

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, a):
        if a > 0:
            self._quantity = a
        else:
            raise ValueError('Quantity must be more than 0')

    def __accept(self):
        if self.store.items[self.item_name] >= self.quantity:
            self.store.items[self.item_name] -= self.quantity
            self.sum = round((self.quantity * self.shelf_price) * (100 - self.user_discount)/100, 2)
        else:
            return False

    def print_invoice(self):
        if self.__accept() is not False:
            print("=" * 40)
            print(":%-10s%28s:" % ("Invoice ID", self.id))
            print(":%-10s%28s:" % ("Item", self.item_name))
            print(":%-10s%24s usd:" % ("Price", self.shelf_price))
            print(":%-10s%24s pcs:" % ("Quantity", self.quantity))
            if self.user_discount > 0:
                print(":%-10s%27s%%:" % ("Discount", self.user_discount))
            print(":%-10s%24s usd:" % ("Overall", self.sum))
            print(":%-10s%28s:" % ("Date", self.date[3:].replace("  ", ",")))
            print("=" * 40)
        else:
            raise ValueError('Not enough goods')
