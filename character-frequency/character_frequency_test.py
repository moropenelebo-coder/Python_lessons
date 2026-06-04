import unittest
from character_frequency import*

# Unit test class for the frequency function
class TestFrequency(unittest.TestCase):

    # Test a normal word with repeated characters
    def test_normal_word(self):
        self.assertEqual(
            frequency("sentence"),
            {'s': 1, 'e': 3, 'n': 2, 't': 1, 'c': 1}
        )

    # Test an empty string
    def test_empty_string(self):
        self.assertEqual(frequency(""), {})

    # Test a word with all unique characters
    def test_unique_characters(self):
        self.assertEqual(
            frequency("abc"),
            {'a': 1, 'b': 1, 'c': 1}
        )

    # Test a word with only one repeated character
    def test_repeated_character(self):
        self.assertEqual(
            frequency("aaaa"),
            {'a': 4}
        )

    # Test a word containing numbers
    def test_numbers(self):
        self.assertEqual(
            frequency("112233"),
            {'1': 2, '2': 2, '3': 2}
        )


# Run all unit tests
if __name__ == "__main__":
    unittest.main()