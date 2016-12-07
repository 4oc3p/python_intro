from time import asctime
from time import localtime
from Home35 import store


class SellInvoice:

    id = 0
    today = localtime()

    def __init__(self, store, user_discount=0):
        self.item_name = []
        self.quantity = []
        self.shelf_price = []
        self.store = store
        self.user_discount = user_discount
        self.sum = {}
        self.date = asctime()
        self.accepted = False
        SellInvoice.id += 1
        self.invoice_number = "%d/%d/%d/%d" % (SellInvoice.id, SellInvoice.today[2],
                                   SellInvoice.today[1], SellInvoice.today[0] % 100)

    def add_item(self, item, quantity):
        if quantity > 0:
            self.quantity.append(quantity)
            self.item_name.append(item.name)
            self.shelf_price.append(item.shelf_price)
        else:
            raise ValueError('Item %s quantity < 0' % item.name)

    def accept(self):
        for i in range(len(self.item_name)):
            if self.store.items[self.item_name[i]] >= self.quantity[i]:
                self.store.items[self.item_name[i]] -= self.quantity[i]
                self.sum[self.item_name[i]] = self.sum.get(self.item_name[i], 0) + round((self.quantity[i] * self.shelf_price[i]) * (100 - self.user_discount)/100, 2)
                self.accepted = True
            else:
                raise ValueError('No such %s in store' % self.item_name[i])

    def cancel(self):
        for i in range(len(self.item_name)):
            self.store.items[self.item_name[i]] += self.quantity[i]
            self.accepted = False
        self.sum.clear()

    def print_invoice(self):
        print("=" * 40)
        print(":%-10s%28s:" % ("Invoice ID", self.invoice_number))
        print(":%-10s%28s:" % ("Item(s)", ','.join(self.item_name)))
        print(":%-10s%24s usd:" % ("Price", self.shelf_price))
        print(":%-10s%24s pcs:" % ("Quantity", self.quantity))
        if self.user_discount > 0:
            print(":%-10s%27s%%:" % ("Discount", self.user_discount))
        print(":%-10s%24s usd:" % ("Overall", sum(self.sum.values())))
        print(":%-10s%28s:" % ("Date", self.date[3:].replace("  ", ",")))
        print(":Invoice %-11s is %15s:" % (self.invoice_number, ("NOT ACCEPTED", "ACCEPTED")[self.accepted]))
        print("=" * 40)
