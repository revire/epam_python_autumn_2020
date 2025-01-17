"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    idx = [x for x in range(k)]
    sums = [
        nums[idx[0] + x] + nums[idx[1] + x] + nums[idx[2] + x]
        for x in range(len(nums) - k + 1)
    ]
    return max(sums)


# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
#
# print(find_maximal_subarray_sum(nums, k))
