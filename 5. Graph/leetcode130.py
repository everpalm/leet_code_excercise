'''
130. Surrounded Regions
Medium

Topics
Companies
You are given an m x n matrix board containing letters 'X' and 'O', capture
regions that are surrounded:

**Connect: A cell is connected to adjacent cells horizontally or vertically.
**Region: To form a region connect every 'O' cell.
**Surround: The region is surrounded with 'X' cells if you can connect the
region with 'X' cells and none of the region cells are on the edge of the
board.
A surrounded region is captured by replacing all 'O's with 'X's in the input
matrix board.

Example 1:
Input: board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]
Output: [["X","X","X","X"],
         ["X","X","X","X"],
         ["X","X","X","X"],
         ["X","O","X","X"]]
Explanation:
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
 
Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
'''
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != 'O':
                return
            board[row][col] = 'T'
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        # Mark the unsurrounded regions with 'T'
        for i in range(m):
            for j in range(n):
                if (i in [0, m-1] or j in [0, n-1]) and board[i][j] == 'O':
                    dfs(i, j)

        # Flip the remaining 'O' to 'X' and 'T' back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'


solution = Solution()
board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]

solution.solve(board)
print('Result1 = ', board)

