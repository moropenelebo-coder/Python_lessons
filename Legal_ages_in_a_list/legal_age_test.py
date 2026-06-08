import unittest
from legal_age import legal_age

class TestLegalAge(unittest.TestCase):

    # Test normal mixed ages
    def test_mixed_ages(self):
        self.assertEqual(
            legal_age([1, 18, 21, 9, 5, 4, 45]),
            [18, 21, 45]
        )

    # Test all ages below legal limit
    def test_all_underage(self):
        self.assertEqual(
            legal_age([1, 2, 3, 10, 17]),
            []
        )

    # Test all ages are legal
    def test_all_legal(self):
        self.assertEqual(
            legal_age([18, 20, 25, 30]),
            [18, 20, 25, 30]
        )

    # Test empty list
    def test_empty_list(self):
        self.assertEqual(
            legal_age([]),
            []
        )

    # Test boundary case (exactly 18 included)
    def test_boundary_age(self):
        self.assertEqual(
            legal_age([17, 18, 19]),
            [18, 19]
        )

# Run tests
if __name__ == "__main__":
    unittest.main()