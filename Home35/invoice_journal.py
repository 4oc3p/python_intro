class InvoiceJournal:

    #=================================================================
    def __init__(self):
        self.invoices = []

    #=================================================================
    def add_invoice(self, sell_invoice):
        if sell_invoice not in self.invoices:
            self.invoices.append(sell_invoice)
