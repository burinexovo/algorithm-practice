from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_heights = [height[0]] * len(height)
        max_right_heights = [height[-1]] * len(height)

        for i in range(1, len(height)):
            max_left_heights[i] = max(max_left_heights[i - 1], height[i])

        for i in range(len(height) - 2, -1, -1):
            max_right_heights[i] = max(max_right_heights[i + 1], height[i])

        result = 0
        for i in range(len(height)):
            result += min(max_left_heights[i], max_right_heights[i]) - height[i]

        return result

# Example 1:
# height = [0,2,0,3,1,0,1,3,2,1]
# Output: 9
