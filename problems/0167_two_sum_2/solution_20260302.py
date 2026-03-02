'''
LeetCode 0167 - Two Sum 2
NeetCode: Two Pointers
Date: 2026-03-02
Time: 7 min
Status: 👀 Hint
Time Complexity: O(n)
Space Complexity: O(1)
'''

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            num_sum = numbers[left] + numbers[right]
            if num_sum == target:
                return [left + 1, right + 1]

            if num_sum > target:
                right -= 1
            else:
                # numbers[left] + numbers[right] < target:
                left += 1


if __name__ == "__main__":
    # Example 1:
    numbers = [1, 2, 3, 4]
    target = 3

    print(Solution().twoSum(numbers=numbers, target=target))
    # Output: [1, 2]
    # Explanation:
    # The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].
