class Person(object):

    def __init__(self, fullname, birthdate, email, phone_number):
        self.fullname = fullname
        self.birthdate = birthdate
        self.email = email
        self.phone_number = phone_number

    def print_info(self):
        print("Name: %s\n"
              "Birthdate: %s\n"
              "Email: %s\n"
              "Phone number: %s\n" % (self.fullname, self.birthdate, self.email, self.phone_number))