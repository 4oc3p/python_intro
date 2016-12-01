from Home34 import vehicle, car, plane

car1 = car.Car(speed_limit=180,
               fuel_consumption=11,
               fuel_tank_size=76,
               number_of_seats=5,
               country_of_origin="Japan")

car2 = car.Car(speed_limit=160,
               fuel_consumption=15,
               fuel_tank_size=89,
               number_of_seats=9,
               country_of_origin="USA")

plane1 = plane.Plane(speed_limit=600,
                     fuel_consumption=400,
                     fuel_tank_size=20000,
                     number_of_seats=120,
                     service_ceiling=13450,
                     current_alt=12222)

plane2 = plane.Plane(speed_limit=740,
                     fuel_consumption=420,
                     fuel_tank_size=24330,
                     number_of_seats=154,
                     service_ceiling=16200,
                     current_alt=18000)


car1.print_info()
car2.print_info()
plane1.print_info()
plane2.print_info()
plane2.decrease_alt()
plane2.print_info()
