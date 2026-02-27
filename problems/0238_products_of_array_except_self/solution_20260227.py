'''
LeetCode 0238 Products of Array Except Self
NeetCode: Arrays & Hashing
Date: 2026-02-27
Time: 7 min
Status: 👀 Hint
Time Complexity: O(nlogn)
Space Complexity: O(n)
'''

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        # prefix: [1, 1, 2, 8]
        # suffix: [48, 24, 6, 1]
        # [48, 24, 12, 8]
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]  # next prefix

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


if __name__ == "__main__":
    # Example 1:
    nums = [1, 2, 4, 6]
    print(Solution().productExceptSelf(nums=nums))
    # Output: [48,24,12,8]

    # Example 2:
    nums = [-1, 0, 1, 2, 3]
    print(Solution().productExceptSelf(nums=nums))
    # Output: [0,-6,0,0,0]
