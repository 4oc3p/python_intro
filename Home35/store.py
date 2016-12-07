class Store:

    def __init__(self):
        self.items = {}  # key = item_name, value = quantity
        self.margin = {}  # key = item_name, value = margin

    def supply(self, item, quantity):
        self.margin[item.name] = self.margin.get(item.name, item.shelf_price - item.cost_price)
        if quantity > 0:
            self.items[item.name] = self.items.get(item.name, 0) + quantity

    def print_status(self):
        for item in sorted(self.items):
            print("Количество %s - %d шт." % (item, self.items[item]))