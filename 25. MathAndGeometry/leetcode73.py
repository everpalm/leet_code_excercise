'''
73. Set Matrix Zeroes
Medium

Hint
Given an m x n integer matrix matrix, if an element is 0, set its entire row
and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''
from typing import List


class Solution:
    def setZeroes_brute_forced(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        x_map = set()
        y_map = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    x_map.add(i)
                    y_map.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in x_map or j in y_map:
                    matrix[i][j] = 0
    
    def setZeroes_optimal(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        # 标记第一行和第一列是否需要置为0
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # 标记其他行和列是否需要置为0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 根据标记置为0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 处理第一行和第一列
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print("Original matrix:")
    for row in matrix:
        print(row)
    
    # 测试暴力解法
    matrix1 = [row[:] for row in matrix]  # 创建深拷贝
    sol.setZeroes_brute_forced(matrix1)
    print("\nAfter brute force solution:")
    for row in matrix1:
        print(row)
    
    # 测试最优解法
    matrix2 = [row[:] for row in matrix]  # 创建深拷贝
    sol.setZeroes_optimal(matrix2)
    print("\nAfter optimal solution:")
    for row in matrix2:
        print(row)
    