from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            my_dict[key].append(s)
        
        return list(my_dict.values())


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
