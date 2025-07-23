import unittest
from L15_index_operator import fruits

# test_L15_index_operator.py


class TestFruitsList(unittest.TestCase):
    def test_index_of_apple(self):
        self.assertEqual(fruits.index("apple"), 0)

    def test_first_element(self):
        self.assertEqual(fruits[0], "apple")

    def test_third_element(self):
        self.assertEqual(fruits[2], "cherry")

    def test_apple_count(self):
        self.assertEqual(fruits.count("apple"), 2)

if __name__ == "__main__":
    unittest.main()
# L15_index_operator_unit_test.py