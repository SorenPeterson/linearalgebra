import unittest
import math
from vector import Vector

class TestVectorMethods(unittest.TestCase):
    def test_addition(self):
        sum_vector = Vector([8.218, -9.341]) + Vector([-1.129, 2.111])
        self.assertEqual(sum_vector.round(3), Vector([7.089, -7.23]))

    def test_subraction(self):
        difference_vector = Vector([7.119, 8.215]) - Vector([-8.223, 0.878])
        self.assertEqual(difference_vector.round(3), Vector([15.342, 7.337]))

    def test_scalar_multiplication(self):
        scaled_vector = Vector([1.671, -1.012, -0.318]) * 7.41
        self.assertEqual(scaled_vector.round(3), Vector([12.382, -7.499, -2.356]))

    def test_magnitude(self):
        magnitude = Vector([-0.221, 7.437]).magnitude()
        self.assertEqual(round(magnitude, 3), 7.44)
        magnitude = Vector([8.813, -1.331, -6.247]).magnitude()
        self.assertEqual(round(magnitude, 3), 10.884)
        zero_vector = Vector([0, 0, 0])
        self.assertEqual(zero_vector.magnitude(), 0)

    def test_direction(self):
        direction = Vector([5.581, -2.136]).direction()
        self.assertEqual(direction.round(3), Vector([0.934, -0.357]))
        direction = Vector([1.996, 3.108, -4.554]).direction()
        self.assertEqual(direction.round(3), Vector([0.340, 0.530, -0.777]))
        direction = Vector([0, 0, 0]).direction()
        self.assertEqual(direction, None)

    def test_dot_product(self):
        dot_product = Vector([7.887, 4.138]) * Vector([-8.802, 6.776])
        self.assertEqual(round(dot_product, 3), -41.382)
        dot_product = Vector([-5.955, -4.904, -1.874]) * Vector([-4.496, -8.755, 7.103])
        self.assertEqual(round(dot_product, 3), 56.397)
        dot_product = Vector([0, 0, 0]) * Vector([-5.955, -4.904, -1.874])
        self.assertEqual(dot_product, 0)

    def test_angle(self):
        angle = Vector([3.183, -7.627]).angle(Vector([-2.668, 5.319]))
        self.assertEqual(round(angle, 3), 3.072)
        angle = Vector([7.35, 0.221, 5.188]).angle(Vector([2.751, 8.259, 3.985]))
        self.assertEqual(round(math.degrees(angle), 3), 60.276)
        angle = Vector([7.35, 0.221, 5.188]).angle(Vector([0, 0, 0]))
        self.assertEqual(angle, None)
        angle = Vector([0, 0, 0]).angle(Vector([7.35, 0.221, 5.188]))
        self.assertEqual(angle, None)

    def test_parallel(self):
        is_parallel = Vector([0, 0, 0]).parallel(Vector([1, 2, 3]))
        self.assertEqual(is_parallel, True)
        is_parallel = Vector([1, 2, 3]).parallel(Vector([0, 0, 0]))
        self.assertEqual(is_parallel, True)
        is_parallel = Vector([1, 2, 3]).parallel(Vector([-1, -2, -3]))
        self.assertEqual(is_parallel, True)
        is_parallel = Vector([1, 2, 3]).parallel(Vector([1, 2, 4]))
        self.assertEqual(is_parallel, False)

    def test_orthogonal(self):
        is_orthogonal = Vector([0, 0, 0]).orthogonal(Vector([0, 0, 0]))
        self.assertEqual(is_orthogonal, True)
        is_orthogonal = Vector([1, 2, 3]).orthogonal(Vector([0, 0, 0]))
        self.assertEqual(is_orthogonal, True)
        is_orthogonal = Vector([0, 0, 0]).orthogonal(Vector([1, 2, 3]))
        self.assertEqual(is_orthogonal, True)
        is_orthogonal = Vector([5, -1, -1]).orthogonal(Vector([1, 2, 3]))
        self.assertEqual(is_orthogonal, True)

    def test_projection(self):
        v = Vector([3.009, -6.172, 3.692, -2.51])
        b = Vector([6.404, -9.144, 2.759, 8.718])
        v_component_parallel_to_b = b.projection(v)
        self.assertEqual(v_component_parallel_to_b, Vector([1.969, -2.811, 0.848, 2.68]))
        v_component_orthogonal_to_b = v - b.projection(v)
        self.assertEqual(v_component_orthogonal_to_b, Vector([1.04, -3.361, 2.844, -5.19]))

if __name__ == '__main__':
    unittest.main()
