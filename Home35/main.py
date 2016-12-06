from Home35.item import Item
from Home35.store import Store
from Home35.sellinvoice import SellInvoice

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

invoice1 = SellInvoice(item=item1,
                       quantity=7,
                       store=store1)
invoice2 = SellInvoice(item=item2,
                       quantity=5,
                       store=store1,
                       user_discount=13)

invoice1.print_invoice()
invoice2.print_invoice()
