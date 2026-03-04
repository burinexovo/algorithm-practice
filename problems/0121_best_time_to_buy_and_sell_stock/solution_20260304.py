'''
LeetCode 0121 - Best Time to Buy and Sell Stock
Topic: Array
Date: 2026-03-04
Time: 5 min
Status: ✅ Solved
Time Complexity: O(n)
Space Complexity: O(1)
'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(prices[i] - min_price, max_profit)

        return max_profit


if __name__ == "__main__":
    # Example 1:
    prices = [10, 1, 5, 6, 7, 1]
    print(Solution().maxProfit(prices=prices))
    # Output: 6
    # Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

    # Example 2:
    prices = [10, 8, 7, 5, 2]
    print(Solution().maxProfit(prices=prices))
    # Output: 0
