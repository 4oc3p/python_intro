from Test2.printedproduction import PrintedProduction


class Statistics(object):

    def __init__(self, registry):
        self.registry = registry.regforms

    def person_stat(self, person):
        sum_books = 0
        sum_magazines = 0
        for regform in self.registry:
            if regform.give_back_date is None and regform.person == person:
                for product in regform.result():
                    if product.type is PrintedProduction.Type.Book.name:
                        sum_books += regform.temp()[product]
                    elif product.type is PrintedProduction.Type.Magazine.name:
                        sum_magazines += regform.temp()[product]
        print("Person %s has %d books and %d magazines" % (person.fullname, sum_books, sum_magazines))

    def person_most_read(self):
        most_readers = {}
        for regform in self.registry:
            if regform.give_back_date is not None and regform.opened is False:
                most_readers[regform.person] = most_readers.get(regform.person, 0) + sum(regform.result().values())

        for person in sorted(most_readers, key=most_readers.get, reverse=True):
            print("%s has read the most" % person.fullname)
            break

    def product_most_read(self):
        most_read_product = {}
        for regform in self.registry:
            for product in regform.result():
                most_read_product[product] = most_read_product.get(product, 0) + regform.result()[product]

        book = 1
        mag = 1
        for product in sorted(most_read_product, key=most_read_product.get, reverse=True):
            if book == 1 and product.type is PrintedProduction.Type.Book.name:
                print("Most read book is %s" % product.title)
                book = 0
            if mag == 1 and product.type is PrintedProduction.Type.Magazine.name:
                print("Most read magazine is %s" % product.title)
                mag = 0
            if mag and book is not True:
                break

    def books_or_magazines(self):
        most_read_product = {}
        for regform in self.registry:
            for product in regform.result():
                most_read_product[product] = most_read_product.get(product, 0) + regform.result()[product]

        for product in sorted(most_read_product, key=most_read_product.get, reverse=True):
            print("People read %s(s) more" % product.type)
            break
