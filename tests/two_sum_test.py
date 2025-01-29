import pytest
from src.two_sum_lc1 import TwoSumSolution

@pytest.fixture
def two_sum_solution():
    return TwoSumSolution()

def test_two_sum_solution(two_sum_solution):
    assert two_sum_solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum_solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert two_sum_solution.twoSum([3, 3], 6) == [0, 1]
    assert two_sum_solution.twoSum([1, 2, 3, 4, 5], 10) == []
    assert two_sum_solution.twoSum([], 0) == []
    assert two_sum_solution.twoSum([1], 1) == []
    assert two_sum_solution.twoSum([1, 2, 3, 4, 5], 8) == [2, 4]