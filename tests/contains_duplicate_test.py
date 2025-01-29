import unittest
from src.contains_duplicate import DuplicateNumbers
from src.contains_duplicate_lc217 import DuplicateNumbers2

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.duplicate_checker = DuplicateNumbers()
        self.duplicate_checker2 = DuplicateNumbers2()

    def test_no_duplicates(self):
        self.assertFalse(self.duplicate_checker.containsDuplicate([1, 2, 3, 4, 5]))
        self.assertFalse(self.duplicate_checker2.containsDuplicate([9, 8, 7, 6, 5]))

    def test_with_duplicates(self):
        self.assertTrue(self.duplicate_checker.containsDuplicate([1, 2, 3, 4, 5, 3]))
        self.assertTrue(self.duplicate_checker2.containsDuplicate([2, 3, 4, 5, 4, 6]))

    def test_empty_list(self):
        self.assertFalse(self.duplicate_checker.containsDuplicate([]))
        self.assertFalse(self.duplicate_checker2.containsDuplicate([]))

    def test_single_element(self):
        self.assertFalse(self.duplicate_checker.containsDuplicate([1]))
        self.assertFalse(self.duplicate_checker2.containsDuplicate([2]))
    def test_all_duplicates(self):
        self.assertTrue(self.duplicate_checker.containsDuplicate([1, 1, 1, 1, 1]))
        self.assertTrue(self.duplicate_checker2.containsDuplicate([10, 10, 10, 10, 10]))

    def test_large_list(self):
        self.assertFalse(self.duplicate_checker.containsDuplicate(list(range(10000))))
        self.assertFalse(self.duplicate_checker2.containsDuplicate(list(range(1000))))
        self.assertTrue(self.duplicate_checker.containsDuplicate(list(range(10000)) + [9999]))
        self.assertTrue(self.duplicate_checker2.containsDuplicate(list(range(1000)) + [999]))

if __name__ == "__main__":
    unittest.main()