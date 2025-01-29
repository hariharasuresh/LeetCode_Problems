from typing import List


class TwoSumSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            num_difference = target - nums[i]
            if num_difference in nums_map:
                return [nums_map[num_difference], i]
            else:
                nums_map[nums[i]] = i
        return []