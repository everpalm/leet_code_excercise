'''
79. Word Search
Medium

Topics
Companies
Given an m x n grid of characters board and a string word, return true if word
exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter
cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
"ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
"SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
"ABCB"
Output: false
 

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a
larger board?
'''
from typing import List

# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         rows, cols = len(board), len(board[0])
        
#         def dfs(index, row, col) -> bool:
#             if index == len(word):
#                 return True
#             if row < 0 or row >= rows or col < 0 or col >= cols:
#                 return False
#             if board[row][col] != word[index]:
#                 return False
            
#             # Mark the cell as visited by replacing the character with a placeholder
#             temp, board[row][col] = board[row][col], '#'
            
#             # Explore the neighbors in the order of up, down, left, right
#             found = (dfs(index + 1, row - 1, col) or
#                      dfs(index + 1, row + 1, col) or
#                      dfs(index + 1, row, col - 1) or
#                      dfs(index + 1, row, col + 1))
            
#             # Restore the cell's original value
#             board[row][col] = temp
#             return found
        
#         for row in range(rows):
#             for col in range(cols):
#                 if dfs(0, row, col):
#                     return True
#         return False
        #Check if cuurent string is identical with first char ==> 'A'
        #Check adjacent cells ==> call stack for index (0, 1) ==> 'B'
        #Check adjacent cells ==> call stack for index (0, 2) ==> 'C'
        #Check adjacent cells ==> call stack for index (0, 3) ==> False
        #Return to (0,2) call stack for index (1, 2) ==> 'C'
        #Check adjacent cells ==> call stack for index (1, 1) ==> False
        #Check adjacent cells ==> call stack for index (1, 3) ==> False
        #Check adjacent cells ==> call stack for index (2, 2) ==> True
        #Check adjacent cells ==> call stack for index (2, 1) ==> True
            
class Solution:
    def __init__(self):
        self.board = []
        self.word = ""
    
    def exist(self, board, word):
        self.board = board
        self.word = word
        
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.dfs(i, j, 0):
                    return True
        
        return False
    
    def dfs(self, i, j, k):
        if k == len(self.word):
            return True
        
        if i < 0 or i >= len(self.board) or j < 0 or j >= len(self.board[0]) \
            or self.board[i][j] != self.word[k]:
            return False
        
        # Mark the cell as visited
        temp = self.board[i][j]
        self.board[i][j] = '#'
        
        # Explore all possible directions
        found = (self.dfs(i + 1, j, k + 1) or
                 self.dfs(i - 1, j, k + 1) or
                 self.dfs(i, j + 1, k + 1) or
                 self.dfs(i, j - 1, k + 1))
        
        # Unmark the cell as visited
        self.board[i][j] = temp
        
        return found

# Example usage:
board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
solution = Solution()
print(solution.exist(board1, word1))  # Output: true

board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "SEE"
print(solution.exist(board2, word2))  # Output: true

board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word3 = "ABCB"
print(solution.exist(board3, word3))  # Output: false
