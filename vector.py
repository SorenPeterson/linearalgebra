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

    def magnitude(self):
        sum_of_squares = 0
        for coordinate in self.coordinates:
            sum_of_squares += coordinate * coordinate
        return math.sqrt(sum_of_squares)

    def direction(self):
        return self * (1 / self.magnitude())

    def angle(self, v):
        return math.acos(self * v / (self.magnitude() * v.magnitude()))

print 'Addition'
print Vector([8.218, -9.341]) + Vector([-1.129, 2.111])
print

print 'Subtraction'
print Vector([7.119, 8.215]) - Vector([-8.223, 0.878])
print

print 'Scalar Multiplication'
print Vector([1.671, -1.012, -0.318]) * 7.41
print

print 'Magnitude'
print Vector([-0.221, 7.437]).magnitude()
print Vector([8.813, -1.331, -6.247]).magnitude()
print

print 'Direction'
print Vector([5.581, -2.136]).direction()
print Vector([1.996, 3.108, -4.554]).direction()
print

print 'Dot Product'
print Vector([7.887, 4.138]) * Vector([-8.802, 6.776])
print Vector([-5.955, -4.904, -1.874]) * Vector([-4.496, -8.755, 7.103])
print

print 'Angle'
print Vector([3.183, -7.627]).angle(Vector([-2.668, 5.319]))
print math.degrees(Vector([7.35, 0.221, 5.188]).angle(Vector([2.751, 8.259, 3.985])))
print
