import unittest
from vector import Vector

class TestVectorMethods(unittest.TestCase):
    def test_addition(self):
        sum_vector = Vector([8.218, -9.341]) + Vector([-1.129, 2.111])
        self.assertEqual(sum_vector, Vector([1, 2, 3]))

if __name__ == '__main__':
    unittest.main()

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
