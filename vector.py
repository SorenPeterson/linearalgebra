import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        new = []
        for pair in zip(*[self.coordinates, v.coordinates]):
            new += [pair[0] + pair[1]]
        return Vector(new)

    def __sub__(self, v):
        new = []
        for pair in zip(*[self.coordinates, v.coordinates]):
            new += [pair[0] - pair[1]]
        return Vector(new)

    def __mul__(self, multiple):
        case = type(multiple)
        if case == Vector:
            return self.__dot_product(multiple)
        else:
            return self.__scalar_product(multiple)

    def __dot_product(self, v):
        sum_of_products = 0
        for pair in zip(*[self.coordinates, v.coordinates]):
            sum_of_products += pair[0] * pair[1]
        return sum_of_products

    def __scalar_product(self, scalar):
        new = []
        for coordinate in self.coordinates:
            new += [coordinate * scalar]
        return Vector(new)

    def round(self, places):
        new = []
        for coordinate in self.coordinates:
            new += [round(coordinate, places)]
        return Vector(new)

    def magnitude(self):
        sum_of_squares = 0
        for coordinate in self.coordinates:
            sum_of_squares += coordinate * coordinate
        return math.sqrt(sum_of_squares)

    def direction(self):
        if self.magnitude() == 0:
            return None
        return self * (1 / self.magnitude())

    def angle(self, v):
        multiplied_magnitudes = self.magnitude() * v.magnitude()
        if(multiplied_magnitudes == 0):
            return None
        return math.acos(self * v / multiplied_magnitudes)
