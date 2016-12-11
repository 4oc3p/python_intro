from enum import Enum


class PrintedProduction(object):

    class Type(Enum):
        Book = 1
        Magazine = 2

    id = 0

    def __init__(self, title, isbn, type=None):
        self.title = title
        self.isbn_code = isbn
        self.type = type
        PrintedProduction.id += 1
        self.id = PrintedProduction.id

    def _print(self):
        print("ID: %d\n"
              "Title: %s\n"
              "ISBN: %s" % (self.id, self.title, self.isbn_code))


class Book(PrintedProduction):

    def __init__(self, title, isbn, writer):
        super().__init__(title, isbn, super().Type.Book.name)
        self.writer = writer

    def print_info(self):
        self._print()
        print("Writer: %s" % self.writer)


class Magazine(PrintedProduction):

    def __init__(self, title, isbn, date):
        super().__init__(title, isbn, super().Type.Magazine.name)
        self.date = date

    def print_info(self):
        self._print()
        print("Date: %s" % self.date)