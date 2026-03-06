from typing import List
# 卡 需要加強！！去重不知道怎麼去


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break  # -> 繼續往下走沒用 因為已經排徐

            # 去重 需排序 這樣才有意義。
            if i > 0 and nums[i] == nums[i - 1]:  # 前面已經跑過了 不用跑
                continue

            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                num_sum = nums[left] + nums[right]
                if num_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    # left 去重
                    # 目前的left 跟上一個left 一樣
                    while left < right and nums[left] == nums[left - 1]:  # 前面已經跑過了 不用跑
                        left += 1

                    # right 去重
                    # 目前的right 跟上一個right 一樣
                    while left < right and nums[right] == nums[right + 1]:  # 前面已經跑過了 不用跑
                        right -= 1
                elif num_sum > target:
                    right -= 1
                else:
                    left += 1

        return result


# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
