import unittest
from src.anagram_lc242 import AnagramSolution
from src.anagram_lc242_2 import AnagramSolution2

class TestIsAnagram(unittest.TestCase):
    def setUp(self):
        self.asolution = AnagramSolution()
        self.asolution2 = AnagramSolution2()

    def test_valid_anagrams(self):
        self.assertTrue(self.asolution.isAnagram("listen", "silent"))
        self.assertTrue(self.asolution.isAnagram("anagram", "nagaram"))
        self.assertTrue(self.asolution2.isAnagram("rat", "tar"))

    def test_different_lengths(self):
        self.assertFalse(self.asolution.isAnagram("hello", "helloo"))
        self.assertFalse(self.asolution2.isAnagram("test", "testing"))

    def test_same_letters_different_frequencies(self):
        self.assertFalse(self.asolution.isAnagram("aabbcc", "aabbc"))
        self.assertFalse(self.asolution2.isAnagram("abc", "aabbcc"))

    def test_empty_strings(self):
        self.assertTrue(self.asolution.isAnagram("", ""))  # Edge case: both are empty
        self.assertTrue(self.asolution2.isAnagram("", ""))  # Edge case: both are empty

    def test_single_character_strings(self):
        self.assertTrue(self.asolution.isAnagram("a", "a"))
        self.assertTrue(self.asolution2.isAnagram("b", "b"))
        self.assertFalse(self.asolution.isAnagram("a", "b"))
        self.assertFalse(self.asolution2.isAnagram("c", "b"))

    def test_case_sensitivity(self):
        self.assertFalse(self.asolution.isAnagram("Hello", "hello"))  # Should return False (case-sensitive)
        self.assertFalse(self.asolution2.isAnagram("World", "world"))  # Should return False (case-sensitive)

if __name__ == "__main__":
    unittest.main()
