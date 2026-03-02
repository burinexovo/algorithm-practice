'''
LeetCode 0125 - Valid Palindrome
NeetCode: TWO Pointers
Date: 2026-03-02
Time: 8 min
Status: 👀 Hint
Time Complexity: O(n)
Space Complexity: O(1)
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # 遇到非 A-Za-z0-9 跳過
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            # 檢查數字跟字母
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    # Example 1:
    s = "Was it a car or a cat I saw?"
    print(Solution().isPalindrome(s=s))
    # Output: true
    # Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

    # Example 2:
    s = "tab a cat"
    print(Solution().isPalindrome(s=s))
    # Output: false
    # Explanation: "tabacat" is not a palindrome.
