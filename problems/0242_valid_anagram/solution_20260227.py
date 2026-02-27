'''
LeetCode 242 Valid Anagram
Topic: Arrays & Hashing
Date: 2026-02-27
Time: 3 min
Status: ✅ Solved
Time Complexity: O(n log n)
Space Complexity: O(n)
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    # Example 1:
    s = "racecar"
    t = "carrace"
    print(Solution().isAnagram(s, t))  # Output: True

    # Example 2:
    s = "jar"
    t = "jam"
    print(Solution().isAnagram(s, t))  # Output: False
