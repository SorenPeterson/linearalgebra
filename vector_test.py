import unittest
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

if __name__ == '__main__':
    unittest.main()
