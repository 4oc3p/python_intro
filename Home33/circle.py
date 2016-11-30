from math import sqrt
from Home33 import point


class Circle:

    def __init__(self, x=0, y=0, radius=5):
        self.center_x = x
        self.center_y = y
        self.radius = radius

    def is_point_of_circle(self, point):
        checking = sqrt((point.x - self.center_x)**2 + (point.y - self.center_y)**2) <= self.radius
        result = ("не принадлежит", "принадлежит")[checking]
        print("Точка с координатами x=%s, y=%s %s окружности с центром x=%s, y=%s и радиусом %s." %
              (point.x, point.y, result, self.center_x, self.center_y, self.radius))
        return checking


