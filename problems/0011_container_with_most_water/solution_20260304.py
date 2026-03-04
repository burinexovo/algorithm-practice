'''
LeetCode 0011 - Container With Most Water
NeetCode: Two Pointers
Date: 2026-03-04
Time: 8 min
Status: 👀 Hint
Time Complexity: O(n)
Space Complexity: O(1)
'''

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        # 試圖找更高的板子
        while left < right:
            area = max(area, min(heights[left], heights[right]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return area


if __name__ == "__main__":
    # Example 2:
    height = [1, 7, 2, 5, 4, 7, 3, 6]
    print(Solution().maxArea(heights=height))
    # Output: 36

    # Example 2:
    height = [2, 2, 2]
    print(Solution().maxArea(heights=height))
    # Output: 4
