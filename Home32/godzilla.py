from Home32 import human


class Godzilla:

    def __init__(self, stomach_limit, name="Godzilla"):
        self.name = name
        self.stomach_limit = stomach_limit
        self.stomach_size = 0
        self.last_hum_weight = 0

    def is_stomach_full(self):
        if self.stomach_size >= self.stomach_limit * 0.9:
            return True
        else:
            return False

    def eat_people(self, human):
        self.last_hum_weight = human.weight
        if Godzilla.is_stomach_full(self):
            print("Не могу больше есть!!! Желудок забит на 90%")
        else:
            self.stomach_size += self.last_hum_weight

    def print_status(self):
        if Godzilla.is_stomach_full(self):
            print("%s уже наелась и хочет спать." % self.name)
        else:
            print("Чудовище, по имени %s съело человека весом %sкг и желудок заполнен на %s%%" %
                  (self.name, self.last_hum_weight, round(self.stomach_size / self.stomach_limit * 100)))
