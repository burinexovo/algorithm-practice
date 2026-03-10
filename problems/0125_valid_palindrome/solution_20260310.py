class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # isalnum() 判斷英文跟數字
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

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
