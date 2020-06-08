import unittest
from src.vector_utils import Vector


class TestVector(unittest.TestCase):

    def test_add(self):
        v1 = [2, 3]
        v2 = [3, 4]
        self.assertEqual([5, 7], Vector.add(v1, v2))

        v1 = [5, 12, 32, 12]
        v2 = [34, 3, 4, 2]
        self.assertEqual([39, 15, 36, 14], Vector.add(v1, v2))

    def test_substract(self):
        v1 = [2, 3]
        v2 = [3, 4]
        self.assertEqual([-1, -1], Vector.subtract(v1, v2))

        v1 = [5, 12, 32, 12]
        v2 = [34, 3, 4, 2]
        self.assertEqual([-29, 9, 28, 10], Vector.subtract(v1, v2))

    def test_distance(self):
        v1 = [7, 4, 3]
        v2 = [17, 6, 2]
        self.assertAlmostEqual(10.24695, Vector.distance(v1, v2), places=4)

        v1 = [23, 43, 12]
        v2 = [45, 21, 10]
        self.assertAlmostEqual(31.176915, Vector.distance(v1, v2), places=4)

    def test_mean(self):
        self.assertEqual([2.0, 2.0], Vector.mean([0, 1], [2, 2], [4, 3]))


if __name__ == '__main__':
    unittest.main()
