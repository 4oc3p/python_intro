from Test2 import person
from Test2 import printedproduction
from Test2 import library
from Test2 import regform
from Test2 import registry
from Test2 import statistics


person1 = person.Person("VOvan", "30.07.1993", "4oc3p@mail.ru", "0638523082")
person2 = person.Person("ALAvan", "30.07.1993", "4oc3p@mail.ru", "0638523082")


book1 = printedproduction.Book("Qer", "123-311-33", "Akkser")
book2 = printedproduction.Book("Qer1q1q", "123-311-33", "Akkser")

magazine1 = printedproduction.Magazine("Trrr", "123-354-22", "21.11.2016")
magazine2 = printedproduction.Magazine("Trsssssrr", "123-354-22", "21.11.2016")

library1 = library.Library()
library1.add_product(book1, 6)
library1.add_product(book2, 4)
library1.add_product(magazine1, 2)
library1.add_product(magazine2, 3)


regform1 = regform.RegForm(person1, library1)
regform2 = regform.RegForm(person2, library1)

regform1.provide(book1, 1)
regform1.provide(magazine1, 1)
regform1.give_back(book1, 1)
regform1.give_back(magazine1, 1)

regform2.provide(book2, 2)
regform2.provide(magazine2, 1)
regform2.give_back(book2, 2)
regform2.give_back(magazine2, 1)

registry1 = registry.Registry()
registry1.add_regform(regform1)
registry1.add_regform(regform2)

statistics1 = statistics.Statistics(registry1)
statistics1.person_stat(person1)
statistics1.person_most_read()
statistics1.product_most_read()
statistics1.books_or_magazines()