
class Vehicle(object):

    def __init__(self, speed_limit, fuel_consumption, fuel_tank_size, number_of_seats):
        self.speed_limit = speed_limit
        self.fuel_consumption = fuel_consumption
        self.fuel_tank_size = fuel_tank_size
        self.number_of_seats = number_of_seats

    def power_reserve(self):
        return round((self.fuel_tank_size / self.fuel_consumption) * 100)

    def print_info(self):
        print("-Емкость бака, л: %s\n"
              "-Расход топлива на 100км, л: %s\n"
              "-Запас хода, км: %s\n"
              "-Максимальная скорость, км/ч: %s\n"
              "-Кол-во мест: %s\n" % (self.fuel_tank_size, self.fuel_consumption, self.power_reserve(),
                                      self.speed_limit, self.number_of_seats))