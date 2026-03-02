'''
LeetCode 0128 - Longest Consecutive Sequence
NeetCode: Arrays & Hashing
Date: 2026-02-28
Time: 20 min
Status: 👀 Hint
Time Complexity: O(n)
Space Complexity: O(n)
'''

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)  # 會讓查詢變 O(1)
        count = 0  # 紀錄最大長度

        # 整體架構 -> 每個數只掃 O(n)
        for num in my_set:
            if num - 1 not in my_set:  # 查詢 O(1)
                # 代表是起點
                length = 1
                while num + length in my_set:
                    length += 1
                count = max(count, length)

        # time O(n) + O(1) => O(n)
        return count


if __name__ == "__main__":

    # Example 1:
    nums = [2, 20, 4, 10, 3, 4, 5]
    print(Solution().longestConsecutive(nums=nums))
    # Output: 4
    # Explanation: The longest consecutive sequence is [2, 3, 4, 5].

    # Example 2:
    nums = [0, 3, 2, 5, 4, 6, 1, 1]
    print(Solution().longestConsecutive(nums=nums))
    # Output: 7
