'''
LeetCode 0271 - Encode and Decode Strings
NeetCode: Arrays & Hashing
Date: 2026-02-27
Time: 10 min
Status: ✅ Solved
Time Complexity: O(n)
Space Complexity: O(m+n)
'''

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""
        for word in strs:
            encoded_strs += str(len(word)) + "#" + word
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):  # 5#Hello5#World
            j = i
            while s[j] != "#":
                j += 1

            end = int(s[i:j])
            result.append(s[j + 1:j + end + 1])  # 要算仔細 index數
            i = end + j + 1  # 0 -> 7
        return result


if __name__ == "__main__":
    # Example 1:

    dummy_input = ["Hello", "World"]

    # Output: ["Hello","World"]
    print(Solution().decode(s=Solution().encode(strs=dummy_input)))

    # Explanation:
    # Machine 1:
    # Codec encoder = new Codec();
    # String msg = encoder.encode(strs);
    # Machine 1 ---msg---> Machine 2

    # Machine 2:
    # Codec decoder = new Codec();
    # String[] strs = decoder.decode(msg);
    # Example 2:

    dummy_input = [""]

    print(Solution().decode(s=Solution().encode(strs=dummy_input)))  # Output: [""]
