'''
LeetCode 0001 - Two Sum
NeetCode: Arrays & Hashing
Date: 2026-02-27
Time: 6 min
Status: ✅ Solved
Time Complexity: O(n)
Space Complexity: O(n)
'''

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dict = {}  # {a: i, ...}

        for i in range(len(nums)):
            # target = a + b
            # b = target - a
            b = target - nums[i]

            if b in temp_dict:  # compare with all pre nums
                return [temp_dict[b], i]

            temp_dict[nums[i]] = i


if __name__ == "__main__":
    # Example 1:
    nums = [3, 4, 5, 6]
    target = 7
    print(Solution().twoSum(nums=nums, target=target))  # Output: [0, 1]

    # Example 2:
    nums = [4, 5, 6]
    target = 10
    print(Solution().twoSum(nums=nums, target=target))  # Output: [0, 2]

    # Example 3:
    nums = [5, 5]
    target = 10
    print(Solution().twoSum(nums=nums, target=target))  # Output: [0, 1]
