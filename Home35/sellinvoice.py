from time import asctime
from time import localtime


class SellInvoice:

    id = 0
    today = localtime()

    def __init__(self, store, user_discount=0):
        self.items = {}  # key = item_name, value = quantity
        self.shelf_price = {}  # key = item_name, value = shelf_price
        self.store = store
        self.user_discount = user_discount
        self.sum = {}  # key = item_name, value = quantity*shelf_price
        self.date = asctime()
        self.accepted = False
        SellInvoice.id += 1
        self.invoice_number = "%d/%d/%d/%d" % (SellInvoice.id, SellInvoice.today[2],
                                               SellInvoice.today[1], SellInvoice.today[0] % 100)

    def add_item(self, item, quantity):
        if quantity > 0:
            self.items[item.name] = self.items.get(item.name, 0) + quantity
            self.shelf_price[item.name] = self.shelf_price.get(item.name, item.shelf_price)
        else:
            raise ValueError('Item %s quantity < 0' % item.name)

    def accept(self):
        for item in self.items:
            if self.store.items[item] >= self.items[item]:
                self.store.items[item] -= self.items[item]
                self.sum[item] = self.sum.get(item, 0) + round((self.items[item] * self.shelf_price[item]) *
                                                               (100 - self.user_discount) / 100, 2)
                self.accepted = True
            else:
                raise ValueError('No such %s in store' % self.items[item])

    def cancel(self):
        for item in self.items:
                self.store.items[item] += self.items[item]
                self.accepted = False
        self.sum.clear()

    def print_invoice(self):
        print("=" * 40)
        print(":%-10s%28s:" % ("Invoice ID", self.invoice_number))
        print(":%-10s%28s:" % ("Item(s)", ','.join(list(sorted(self.items)))))
        print(":%-10s%24s usd:" % ("Price", [self.shelf_price[x] for x in sorted(self.shelf_price)]))
        print(":%-10s%24s pcs:" % ("Quantity", [self.items[x] for x in sorted(self.items)]))
        if self.user_discount > 0:
            print(":%-10s%27s%%:" % ("Discount", self.user_discount))
        print(":%-10s%24s usd:" % ("Overall", sum(self.sum.values())))
        print(":%-10s%28s:" % ("Date", self.date[3:].replace("  ", ",")))
        print(":Invoice %-11s is %15s:" % (self.invoice_number, ("NOT ACCEPTED", "ACCEPTED")[self.accepted]))
        print("=" * 40)
