import datetime

class Report(object):

    #=================================================================
    def __init__(self, invoice_journal):
        self.invoice_journal = invoice_journal

    #=================================================================
    def profit_by_item(self, date1, date2):
        print("Profit report from %s till %s:" % (date1, date2))

        item_profit = {}
        for invoice in self.invoice_journal.invoices:
            if date1 < invoice.date.date() < date2:
                disc_coeff = (100 - invoice.user_discount)/100
                for record in invoice.records.values():
                    item_profit[record.item] = item_profit.get(record.item, 0) + \
                                               record.qty * record.item.margin() * disc_coeff

        for item in item_profit:
            print("Прибыль для товара %s = %d usd" % (item.name, item_profit[item]))
        print("Общая прибыль: %d usd" % sum(item_profit.values()))

    #=================================================================
    def total_sale(self, date1=None, date2=None):
        pass

    #=================================================================
    def sale_by_date(self, date1=None, date2=None):
        pass

    #=================================================================
    def sale_by_client(self, date1=None, date2=None, client=None):
        pass

    #=================================================================
    def profit_by_date(self, date1=None, date2=None):
        pass

    #=================================================================
    def profit_by_client(self, date1=None, date2=None):
        pass

    #=================================================================
    def current_balance(self, balance_date=datetime.datetime.now().date()):
        pass