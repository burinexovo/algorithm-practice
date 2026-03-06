'''
LeetCode 0115 - Min Stack
NeetCode: Stack
Date: 2026-03-06
Time: 10 min
Status: 👀 Hint
Time Complexity: O(1)
Space Complexity: O(n)
'''


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            curr_min = min(val, self.stack[-1][1])  # 最上面的[1] (val, min_val) 
            self.stack.append((val, curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == "__main__":
    # Example 1:
    my_list = ["MinStack", "push", 1, "push", 2,
               "push", 0, "getMin", "pop", "top", "getMin"]

    # Output: [null,null,null,null,0,null,2,1]

    # Explanation:
    # MinStack minStack = new MinStack();
    # minStack.push(1);
    # minStack.push(2);
    # minStack.push(0);
    # minStack.getMin(); // return 0
    # minStack.pop();
    # minStack.top();    // return 2
    # minStack.getMin(); // return 1
