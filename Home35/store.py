from Home35 import item


class Store:

    def __init__(self):
        self.items = {}

    def supply(self, item, quantity):
        if quantity > 0:
            self.items[item.name] = self.items.get(item.name, 0) + quantity

    def print_status(self):
        for item in sorted(self.items):
            print("Количество %s - %d шт." % (item, self.items[item]))