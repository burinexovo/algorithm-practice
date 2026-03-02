'''
LeetCode 0015 - 3Sum
NeetCode: Two Pointers
Date: 2026-03-02
Time: 20 min
Status: 👀 Hint
Time Complexity: O(n^2)
Space Complexity: O(1)
'''

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # 排序
        nums.sort()
        for i in range(len(nums)):
            # 剪枝
            if nums[i] > 0:
                break
            # 去重 需排序 這樣才有意義。
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                num_sum = nums[left] + nums[right]

                if num_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # left 去重
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # right 去重
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif num_sum > target:
                    right -= 1
                else:  # num_sum < target
                    left += 1

        return result


if __name__ == "__main__":
    # Example 1:
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums=nums))
    # Output: [[-1,-1,2],[-1,0,1]]
    # Explanation:
    # nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    # nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    # nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    # The distinct triplets are [-1,0,1] and [-1,-1,2].

    # Example 2:
    nums = [0, 1, 1]
    print(Solution().threeSum(nums=nums))
    # Output: []
    # Explanation: The only possible triplet does not sum up to 0.
