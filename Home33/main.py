from Home33 import circle
from Home33 import point

point1 = point.Point(6, 0)
point2 = point.Point(3, 6)
circle1 = circle.Circle(1, 4, 5)

circle1.is_point_of_circle(point1)
circle1.is_point_of_circle(point2)