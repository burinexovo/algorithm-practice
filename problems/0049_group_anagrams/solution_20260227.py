'''
LeetCode 0049 - Group Anagrams
NeetCode: Arrays & Hashing
Date: 2026-02-27
Time: 20 min
Status: 👀 Hint
Time Complexity: O(n)
Space Complexity: O(n)
'''

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            groups[key].append(strs[i])

        return list(groups.values())


if __name__ == "__main__":
    # Example 1:
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    print(Solution().groupAnagrams(strs=strs))

    # Example 2:
    strs = ["x"]
    print(Solution().groupAnagrams(strs=strs))  # Output: [["x"]]

    # Example 3:
    strs = [""]
    print(Solution().groupAnagrams(strs=strs))  # Output: [[""]]
