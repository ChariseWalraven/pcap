# Scenario
# Now we're going to embed the Point class (see Lab 3.4.1.14) inside another class. Also, we're going to put three
# points into one class, which will let us define a triangle. How can we do it?

# The new class will be called Triangle and this is the list of our expectations:

# - the constructor accepts three arguments - all of them are objects of the Point class;
# - the points are stored inside the object as a private list;
# - the class provides a parameterless method called perimeter(), which calculates the perimeter of the triangle
# described by the three points; the perimeter is a sum of all legs' lengths (we mention it for the record, although we
# are sure that you know it perfectly yourself.)

import math  # noqa
from LAB_points_on_a_plane import Point


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__points = [vertice1, vertice2, vertice3, ]

    def perimeter(self):
        # lengths of the sides of the triangle = distance between vertices
        # perimeter = sum of lengths
        # NOTE: I'm not sure this list comprehension thing is the most readable. If anyone ever tries to understand
        # this and I'm not dead, please just ask me 💀
        return sum([self.__points[i].distance_from_point(
            self.__points[i - 1]) for i in range(len(self.__points) - 1, -1, -1)])


if __name__ == '__main__':
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle.perimeter())

# Expected Output
# 3.414213562373095
