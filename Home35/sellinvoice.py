# from time import asctime
# from time import localtime
import datetime


class SellInvoice(object):

    #=================================================================
    class Record(object):

        def __init__(self, item, qty, price, sum):
            self.item = item
            self.qty = qty
            self.price = price
            self.sum = sum

    id = 0
    PRINT_DELIM         = "=" * 40
    FMT_HEADER          = ":%-10s%28s:"
    FMT_RECORD_HEADER   = ":%-10s%6s:"
    FMT_RECORD_LINE     = ":%-10s%-10s%-9s%-9s:"

    #=================================================================
    def __init__(self, store, user_discount=0):

        self.records = {}  # key = item id, value = record
        self.store = store
        self.user_discount = user_discount
        self.date = datetime.datetime.now()
        self.accepted = False
        SellInvoice.id += 1
        self.invoice_number = "%d/%s" % (SellInvoice.id, self.date.strftime("%y/%m/%d"))

    #=================================================================
    def add_item(self, item, quantity):
        if quantity > 0:
            if item in self.records:
                self.records[item].qty += quantity
                self.records[item].sum = self.records[item.id].qty * \
                                         self.records[item.id].price
            else:
                self.records[item] = self.Record( item,
                                                    quantity,
                                                    item.shelf_price,
                                                    item.shelf_price*quantity)
        else:
            raise ValueError('Item %s quantity < 0' % item.name)

    #=================================================================
    def accept(self):
        for record in self.records.values():
            item = record.item
            if self.store.balance(item) >= record.qty:
                self.store.withdraw(item, record.qty)
            else:
                raise ValueError('No such %s in store' % item)
        self.accepted = True

    #=================================================================
    def cancel(self):
        for item in self.items:
                self.store.accept(item, record.qty)
        self.accepted = False

    #=================================================================
    def print_invoice(self):
        print(SellInvoice.PRINT_DELIM)
        print(SellInvoice.FMT_HEADER % ("Invoice ID", self.invoice_number))
        if self.user_discount > 0:
            print(":%-10s%27s%%:" % ("Discount", self.user_discount))
        print(":%-10s%24s usd:" % ("Overall", sum(r.sum for r in self.records.values())))
        print(SellInvoice.FMT_HEADER % ("Date", self.date.strftime("%Y/%M/%D")))
        print(":Invoice %-11s is %15s:" % (self.invoice_number, ("NOT ACCEPTED", "ACCEPTED")[self.accepted]))
        print(SellInvoice.PRINT_DELIM)

        print(SellInvoice.FMT_RECORD_HEADER % ("Title     Qty       Price    Sum", ""))
        for record in self.records.values():
            print(SellInvoice.FMT_RECORD_LINE % (record.item.name,
                                                 record.qty,
                                                 record.price,
                                                 record.sum))
        print(SellInvoice.PRINT_DELIM)
