'''
48. Rotate Image
Medium

Topics
premium lock icon
Companies
You are given an n x n 2D matrix representing an image, rotate the image by 90
degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the
input 2D matrix directly. DO NOT allocate another 2D matrix and do the
rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 
Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
'''
from typing import List

class Solution:
    def rotate_brute_force(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        new_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_matrix[j][n - 1 - i] = matrix[i][j]
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = new_matrix[i][j]

    def rotate_optimal(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Step 1: 轉置矩陣
        for i in range(n):
            for j in range(i + 1, n):  # 注意是 j > i
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: 每列左右反轉
        for row in matrix:
            row.reverse()

if __name__ == "__main__":
    print("Optimal Solution:")
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    solution = Solution()
    solution.rotate_optimal(matrix)
    print(matrix)  # [[7,4,1],[8,5,2],[9,6,3]]
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution.rotate_optimal(matrix)
    print(matrix)  # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    print("Brute Force Solution:")
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    solution.rotate_brute_force(matrix)
    print(matrix)  # [[7,4,1],[8,5,2],[9,6,3]]
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution.rotate_brute_force(matrix)
    print(matrix)  # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    