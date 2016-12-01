from Home34.vehicle import Vehicle


class Car(Vehicle):
    id = 0

    def __init__(self, speed_limit, fuel_consumption, fuel_tank_size, number_of_seats, country_of_origin):
        Vehicle.__init__(self, speed_limit, fuel_consumption, fuel_tank_size, number_of_seats)
        self.country_of_origin = country_of_origin
        Car.id += 1
        self.id = Car.id

    def is_driver_license_b(self):
        return self.number_of_seats <= 9

    def print_info(self):
        print("Автомобиль №%d:\n"
              "-Cтрана производства: %s\n"
              "-Нужны права категории: '%s'" % (self.id, self.country_of_origin, ("D", "B")[self.is_driver_license_b()]))
        Vehicle.print_info(self)
