from Home32 import godzilla
from Home32 import human


human1 = human.Human()
human2 = human.Human()
human3 = human.Human()
human4 = human.Human()
human5 = human.Human()
human6 = human.Human()

godzilla1 = godzilla.Godzilla(500, "Godzilla")


godzilla1.eat_people(human1)
godzilla1.print()
godzilla1.eat_people(human2)
godzilla1.print()
godzilla1.eat_people(human3)
godzilla1.print()
godzilla1.eat_people(human4)
godzilla1.print()
godzilla1.eat_people(human5)
godzilla1.print()
godzilla1.eat_people(human6)
godzilla1.print()