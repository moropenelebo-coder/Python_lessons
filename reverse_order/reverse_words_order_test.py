import unittest
from reverse_words_order import *

class TestReverseWordsOrder(unittest.TestCase):

    # Test a normal sentence with three words
    def test_three_words(self):
        self.assertEqual(
            reverse_words_order("python world hello"),
            "hello world python"
        )

    # Test a sentence with two words
    def test_two_words(self):
        self.assertEqual(
            reverse_words_order("hello world"),
            "world hello"
        )

    # Test a sentence with one word
    def test_one_word(self):
        self.assertEqual(
            reverse_words_order("python"),
            "python"
        )

    # Test an empty string
    def test_empty_string(self):
        self.assertEqual(
            reverse_words_order(""),
            ""
        )

    # Test a sentence with extra spaces
    def test_extra_spaces(self):
        self.assertEqual(
            reverse_words_order("  hello   world  python  "),
            "python world hello"
        )

# Run all tests
if __name__ == "__main__":
    unittest.main()