from Home34.vehicle import Vehicle
from time import sleep


class Plane(Vehicle):
    id = 0

    def __init__(self, speed_limit, fuel_consumption, fuel_tank_size, number_of_seats, service_ceiling, current_alt):
        Vehicle.__init__(self, speed_limit, fuel_consumption, fuel_tank_size, number_of_seats)
        self.service_ceiling = service_ceiling
        # self._current_alt = 0
        self.current_alt = current_alt
        Plane.id += 1
        self.id = Plane.id

    # @property
    # def current_alt(self):
    #     return self._current_alt
    #
    # @current_alt.setter
    # def current_alt(self, current_alt):
    #     if current_alt > self.service_ceiling:
    #         self.decrease_alt()
    #     else:
    #         self._current_alt = current_alt

    def decrease_alt(self):
        if self.current_alt <= self.service_ceiling:
            print("OK, alt is %sm\n" % self.current_alt)
        else:
            self.current_alt -= 100
            print("Lower alt for 100m: %sm" % self.current_alt)
            sleep(0.3)
            self.decrease_alt()

    def print_info(self):
        print("-Самолёт №%s\n"
              "-Максимальная высота, м: %d\n"
              "-Текущая высота, м: %s" % (self.id, self.service_ceiling, self.current_alt))
        Vehicle.print_info(self)