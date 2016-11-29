from Home32 import human


class Godzilla:

    def __init__(self, stomach_size, name="Godzilla"):
        self.name = name
        self.stomach_size = stomach_size
        self.empty_stomach = 0
        self.hum_weight = 0

    def eat_people(self, human):
        self.hum_weight = human.weight
        if self.empty_stomach > self.stomach_size * 0.9:
            pass
        else:
            self.empty_stomach += self.hum_weight

    def print(self):
        if self.empty_stomach < self.stomach_size * 0.9:
            print("Чудовище, по имени %s съело ещё одного человеа весом %sкг и заполнила желудок на %s%%" %
                  (self.name, self.hum_weight, round(self.empty_stomach / self.stomach_size * 100)))
        else:
            print("Чудовище уже не может больше есть! Желудок заполнен на %s%%" %
                  round(self.empty_stomach / self.stomach_size * 100))
