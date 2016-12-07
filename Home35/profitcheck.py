class ProfitCheck:

    def __init__(self, store):
        self.item_profit = {}
        self.full_profit = {}
        self.margin = store.margin

    def add_invoice(self, sellinvoice):
        for name in sellinvoice.items:
            self.item_profit[name] = self.item_profit.get(name, sellinvoice.items[name]) * self.margin[name]

    def print_items_profit(self):
        for name in sorted(self.item_profit):
            print("Прибыль для товара %s = %d usd" % (name, self.item_profit[name]))
        print("Общая прибыль: %d usd" % sum(self.item_profit.values()))
