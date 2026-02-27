'''
LeetCode 217 - contains duplicate
Topic: Arrays & Hashing
Date: 2026-02-27
Time: 5 min
Status: ✅ Solved
Time Complexity: O(n)
Space Complexity: O(n)
'''

from typing import List
from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_set = set()
        
        for num in nums:
            if num in freq_set:
                return True
            freq_set.add(num)
        return False

        # Other solution
        # freq_dict = Counter(nums)

        # for k, v in freq_dict.items():
        #     if v > 1:
        #         return True

        # return False


if __name__ == "__main__":
    # Example 1:
    nums = [1, 2, 3, 1]
    print(Solution().hasDuplicate(nums))  # Output: True

    # Example 2:
    nums = [1, 2, 3, 4]
    print(Solution().hasDuplicate(nums))  # Output: False

    # Example 3:
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(Solution().hasDuplicate(nums))  # Output: True
