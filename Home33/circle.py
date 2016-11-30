from math import sqrt
from Home33 import point


class Circle:

    def __init__(self, x=0, y=0, radius=5):
        self.center_x = x
        self.center_y = y
        self.radius = radius
        self.point_x = 0
        self.point_y = 0

    def is_point_in_circle(self):
        return sqrt((self.point_x - self.center_x)**2 + (self.point_y - self.center_y)**2) <= self.radius

    def result_print(self, point):
        self.point_x = point.x
        self.point_y = point.y
        if self.is_point_in_circle():
            result = "принадлежит"
        else:
            result = "не принадлежит"
        print("Точка с координатами x=%s, y=%s %s окружности с центром x=%s, y=%s и радиусом %s." %
                  (self.point_x, self.point_y, result, self.center_x, self.center_y, self.radius))


