class Store:

    #=================================================================
    def __init__(self):
        self._items = {}

    #=================================================================
    def balance(self, item):
        return self._items.get(item, 0)

    #=================================================================
    def supply(self, item, quantity):
        if quantity > 0:
            self._items[item] = self._items.get(item, 0) + quantity

    #=================================================================
    def withdraw(self, item, quantity):
        if quantity <= 0:
            raise ValueError("Negative quantity: ", quantity)

        curr_balance = self._items.get(item, 0)
        if curr_balance >= quantity:
            self._items[item] = curr_balance - quantity
        else:
            raise BaseException("Negative balance: %d->%d" % (curr_balance, quantity))

    #=================================================================
    def print_status(self):
        print("Balance:")
        for item in sorted(self._items, key=lambda item: item.name):
            print("\t%s - %d pcs." % (item.name, self._items[item]))