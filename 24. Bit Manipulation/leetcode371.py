'''371. Sum of Two Integers
Medium

Topics
Companies
Given two integers a and b, return the sum of the two integers without using
the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5
 
Constraints:
-1000 <= a, b <= 1000
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MASK = 0x7FFFFFFF
        a &= MASK
        b &= MASK
        while b:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK
        return a if a <= INT_MASK else ~(a ^ MASK)
    

if __name__ == '__main__':
    sol = Solution()
    a = 1
    b = 2
    print('Example 1 = ', sol.getSum(a, b))  # Expected 3

    a = 2
    b = 3
    print('Example 1 = ', sol.getSum(a, b))  # Expected 5