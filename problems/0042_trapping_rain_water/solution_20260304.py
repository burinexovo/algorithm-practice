'''
LeetCode 0042 - Trapping Rain Water
NeetCode: Two Pointers
Date: 2026-03-04
Time: 30 min
Status: ❌ Failed
Time Complexity: O(n)
Space Complexity: O(n)
'''

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [height[0]] * len(height)
        max_right = [height[-1]] * len(height)

        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i])

        print(max_left)

        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])

        print(max_right)

        result = 0
        for i in range(len(height)):
            result += min(max_left[i], max_right[i]) - height[i]

        return result


if __name__ == "__main__":
    # Example 1:
    height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    print(Solution().trap(height=height))
    # Output: 9
