'''
LeetCode 0036 - Valid Sudoku
NeetCode: Arrays & Hashing
Date: 2026-02-28
Time: 8 min
Status: ✅ Solved
Time Complexity: O(n^2)
Space Complexity: O(n^2)
'''

from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check every row
        row = defaultdict(set)  # {0: {'1', ...}}
        # check every col
        col = defaultdict(set)  # {0 : {'1', ...}}
        # check every 3*3 box
        box = defaultdict(set)  # {(0, 0) : {'1', ...}}

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue

                if board[i][j] in row[i]:
                    return False
                row[i].add(board[i][j])

                if board[i][j] in col[j]:
                    return False
                col[j].add(board[i][j])

                if board[i][j] in box[(i//3, j//3)]:
                    return False
                box[(i//3, j//3)].add(board[i][j])

        return True


if __name__ == "__main__":

    # Example 1:
    board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
             ["4", ".", ".", "5", ".", ".", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", ".", "3"],
             ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
             [".", ".", ".", "8", ".", "3", ".", ".", "5"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", ".", ".", ".", ".", ".", "2", ".", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "8"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(Solution().isValidSudoku(board=board))
    # Output: true

    # Example 2:
    board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
             ["4", ".", ".", "5", ".", ".", ".", ".", "."],
             [".", "9", "1", ".", ".", ".", ".", ".", "3"],
             ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
             [".", ".", ".", "8", ".", "3", ".", ".", "5"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", ".", ".", ".", ".", ".", "2", ".", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "8"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(Solution().isValidSudoku(board=board))
    # Output: false
