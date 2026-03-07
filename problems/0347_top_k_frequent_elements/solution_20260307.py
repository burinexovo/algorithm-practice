from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        bucket = [[] for _ in range(len(nums))]

        for num, cnt in freq.items():
            bucket[cnt].append(num)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                if len(res) == k:
                    return res
                res.append(num)
        return res


# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]
