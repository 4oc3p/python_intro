class Library(object):

    def __init__(self):
        self._content = {}

    def quantity(self, product):
        return self._content.get(product)

    def content(self):
        return self._content

    def add_product(self, product, qty):
        if qty > 0:
            self._content[product] = self._content.get(product, 0) + qty

    def remove_product(self, product, qty):
        if self._content[product] >= qty:
            self._content[product] -= qty
        else:
            raise ValueError("There is no such product")

    def print_content(self):
        for product in sorted(self._content, key=lambda product: product.id):
            print("ID: %d, Type: %s, Title: %s, ISBN: %s. Quantity: %d" %
                  (product.id, product.type, product.title, product.isbn_code, self._content[product]))