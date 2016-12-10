from Home35.sellinvoice import SellInvoice

class Item:

    id = 0

    def __init__(self, name, cost_price, shelf_price):
        self.name = name
        self._cost_price = None
        self.cost_price = cost_price
        self._shelf_price = None
        self.shelf_price = shelf_price
        Item.id += 1
        self.id = Item.id

    @staticmethod
    def is_positive(price):
        return price > 0

    @property
    def cost_price(self):
        return self._cost_price

    @cost_price.setter
    def cost_price(self, price):
        if Item.is_positive(price):
            self._cost_price = price
        else:
            raise ValueError('Incorrect value: %d' % price)

    @property
    def shelf_price(self):
        return self._shelf_price

    @shelf_price.setter
    def shelf_price(self, price):
        if Item.is_positive(price):
            self._shelf_price = price
        else:
            raise ValueError('Incorrect value: %d' % price)

    def margin(self):
        return self.shelf_price - self.cost_price

    def print_info(self):
        print("-"*20)
        print(self)

    def __str__(self):
        return "ID: %d, Name: %s, Price: %d" % (self.id, self.name, self.shelf_price)