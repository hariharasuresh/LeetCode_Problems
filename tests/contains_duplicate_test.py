import unittest
from src.contains_duplicate import DuplicateNumbers

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.duplicate_checker = DuplicateNumbers()

    def test_no_duplicates(self):
        self.assertFalse(self.duplicate_checker.containsDuplicate([1, 2, 3, 4, 5]))

    def test_with_duplicates(self):
        self.assertTrue(self.duplicate_checker.containsDuplicate([1, 2, 3, 4, 5, 3]))

    def test_empty_list(self):
        self.assertFalse(self.duplicate_checker.containsDuplicate([]))

    def test_single_element(self):
        self.assertFalse(self.duplicate_checker.containsDuplicate([1]))

    def test_all_duplicates(self):
        self.assertTrue(self.duplicate_checker.containsDuplicate([1, 1, 1, 1, 1]))

    def test_large_list(self):
        self.assertFalse(self.duplicate_checker.containsDuplicate(list(range(10000))))
        self.assertTrue(self.duplicate_checker.containsDuplicate(list(range(10000)) + [9999]))

if __name__ == "__main__":
    unittest.main()