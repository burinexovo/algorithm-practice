'''
LeetCode 0020 - Valid Parentheses
NeetCode: Stack
Date: 2026-03-06
Time: 10 min
Status: 👀 Hint
Time Complexity: O(n)
Space Complexity: O(n)
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}

        for c in s:
            if c in pairs:
                stack.append(pairs[c])
            else:
                # 代表是 closs 要 pop 出來比較一下
                if not stack or stack.pop() != c:
                    return False

        return not stack

        # stack = []
        # pairs = {']': '[', '}': '{', ')': '('}
        # for c in s:
        #     if c in pairs:
        #         if stack and stack[-1] == pairs[c]:
        #             stack.pop()
        #             print(stack)
        #         else:
        #             return False
        #     else:
        #         # 代表是開始符號
        #         stack.append(c)

        # return not stack # 如果左右對稱已經被pop乾了


if __name__ == "__main__":
    # Example 1:
    s = "[]"
    print(Solution().isValid(s=s))
    # Output: true

    # Example 2:
    s = "([{}])"
    print(Solution().isValid(s=s))
    # Output: true

    # Example 3:
    s = "[(])"
    print(Solution().isValid(s=s))
    # Output: false
