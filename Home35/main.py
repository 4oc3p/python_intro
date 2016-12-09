from datetime import date, timedelta

from Home35.item import Item
from Home35.store import Store
from Home35.sellinvoice import SellInvoice
from Home35.invoice_journal import InvoiceJournal
from Home35.report import Report

item1 = Item(name="Item1",
             cost_price=11,
             shelf_price=22)
item2 = Item(name="Item2",
             cost_price=22,
             shelf_price=44)
item3 = Item(name="Item3",
             cost_price=33,
             shelf_price=66)

store1 = Store()

store1.supply(item=item1,
              quantity=40)
store1.supply(item=item2,
              quantity=80)
store1.supply(item=item3,
              quantity=20)

store1.print_status()

invoice1 = SellInvoice(store=store1)

invoice2 = SellInvoice(store=store1,
                       user_discount=13)

invoice1.add_item(item1, 10)
invoice1.add_item(item3, 10)
invoice1.accept()
invoice1.print_invoice()

invoice2.add_item(item1, 8)
invoice2.add_item(item2, 4)
invoice2.accept()
invoice2.print_invoice()

journal1 = InvoiceJournal()
journal1.add_invoice(invoice1)
journal1.add_invoice(invoice2)

report1 = Report(journal1)
report1.profit_by_item(date.today() - timedelta(days=1),
                       date.today() + timedelta(days=1))
