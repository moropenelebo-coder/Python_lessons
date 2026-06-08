import unittest
from count_negative_numbers import *

class TestCountNegativeNumbers(unittest.TestCase):

    # Test list with positive and negative numbers
    def test_mixed_numbers(self):
        self.assertEqual(
            count_negative_numbers([10, -4, -6, 2, 5, 3, -15, -4]),
            4
        )

    # Test list with no negative numbers
    def test_no_negatives(self):
        self.assertEqual(
            count_negative_numbers([1, 2, 3, 4, 5]),
            0
        )

    # Test list containing only negative numbers
    def test_all_negatives(self):
        self.assertEqual(
            count_negative_numbers([-1, -2, -3, -4]),
            4
        )

    # Test empty list
    def test_empty_list(self):
        self.assertEqual(
            count_negative_numbers([]),
            0
        )

    # Test list with zeros and negative numbers
    def test_zeros_and_negatives(self):
        self.assertEqual(
            count_negative_numbers([0, -1, 0, -2, 0]),
            2
        )

# Run the tests
if __name__ == "__main__":
    unittest.main()


#Run test
#python -m unittest test_count_negative_numbers.py