'''
74. Search a 2D Matrix
Medium

Topics
Companies
You are given an m x n integer matrix matrix with the following two properties
:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous
row. Given an integer target, return true if target is in matrix or false
otherwise.

You must write a solution in O(log(m * n)) time complexity.


Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        print('m = ', len(matrix))
        print('n = ', len(matrix[0]))
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            print('left = ', left)
            print('right = ', right)
            mid_index = (left + right)//2
            row, col = divmod(mid_index, n)
            print('mid_index =', mid_index)
            print('row = ', row)
            print('col = ', col)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid_index + 1
            else:
                right = mid_index - 1
        return False
    

my_solution = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(f'Result1 = {my_solution.searchMatrix(matrix, target)}')

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(f'Result2 = {my_solution.searchMatrix(matrix, target)}')

matrix = [[1,1]]
target = 2
print(f'Result3 = {my_solution.searchMatrix(matrix, target)}')