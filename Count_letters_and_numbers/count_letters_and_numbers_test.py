import unittest
from count_letters_and_numbers import *

class TestCountLettersNumbers(unittest.TestCase):

    # Test normal sentence with letters and numbers
    def test_mixed_sentence(self):
        self.assertEqual(
            count_letters_numbers("Learning python in 2026"),
            (16, 4)
        )

    # Test empty string
    def test_empty_string(self):
        self.assertEqual(count_letters_numbers(""), (0, 0))

    # Test only letters
    def test_only_letters(self):
        self.assertEqual(count_letters_numbers("HelloWorld"), (10, 0))

    # Test only numbers
    def test_only_numbers(self):
        self.assertEqual(count_letters_numbers("123456"), (0, 6))

    # Test mixed with symbols (should ignore symbols)
    def test_symbols_ignored(self):
        self.assertEqual(
            count_letters_numbers("a1!b2@c3#"),
            (3, 3)
        )


# Run tests
if __name__ == "__main__":
    unittest.main()