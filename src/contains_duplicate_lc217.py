from typing import List


class DuplicateNumbers2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))