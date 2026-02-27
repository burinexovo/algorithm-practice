'''
LeetCode 0347 - Top K Frequent Elements
NeetCode: Arrays & Hashing
Date: 2026-02-27
Time: 3 min
Status: ✅ Solved
Time Complexity: O(nlogn)
Space Complexity: O(n)
'''

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        couter = Counter(nums)

        return sorted(couter, key=lambda x: couter[x])[-k:]
        # return sorted(couter, key=lambda x: couter[x])[::-1][:k]
        # return sorted(couter, key=lambda x: couter[x], reverse=True)[:k]
    
        # time O(n)
        # bucket = [[] for i in range(len(nums) + 1)]

        # for num, cnt in couter.items():
        #     bucket[cnt].append(num)

        # result = []
        # for i in range(len(bucket) - 1, 0, -1):
        #     for num in bucket[i]:
        #         result.append(num)
        #         if len(result) == k:
        #             return result
                
        # return result


if __name__ == "__main__":
    # Example 1:
    nums = [1, 2, 2, 3, 3, 3]
    k = 2
    print(Solution().topKFrequent(nums=nums, k=k))  # Output: [3,2]

    # Example 2:
    nums = [7, 7]
    k = 1
    print(Solution().topKFrequent(nums=nums, k=k))  # Output: [7]
