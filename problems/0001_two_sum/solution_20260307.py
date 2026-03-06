from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i in range(len(nums)):
            # target = a + b
            # b = target - a
            b = target - nums[i]

            if b in my_dict:
                pass
                return [my_dict[b], i]

            my_dict[nums[i]] = i

        


# Example 1:
# Input: nums = [3,4,5,6], target = 7
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:
# Input: nums = [4,5,6], target = 10
# Output: [0,2]

# Example 3:
# Input: nums = [5,5], target = 10
# Output: [0,1]