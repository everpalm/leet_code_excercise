'''
191. Number of 1 Bits
Easy

Topics
Companies
Given a positive integer n, write a function that returns the number of set
bits in its binary representation (also known as the Hamming weight).


Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 
Constraints:
1 <= n <= 231 - 1
 Follow up: If this function is called many times, how would you optimize it?
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += (n & 1)
            n >>= 1
        return count
    
    def Optimized(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count
    
if __name__ == '__main__':
    sol = Solution()
    n = 11
    print('Example 1 = ', sol.hammingWeight(n))  # Expected 3
    print('Example 1-1 = ', sol.Optimized(n))  # Expected 3

    n = 128
    print('Example 2 = ', sol.hammingWeight(n))  # Expected 1
    print('Example 2-1 = ', sol.Optimized(n))  # Expected 1

    n = 2147483645
    print('Example 3 = ', sol.hammingWeight(n))  # Expected 30
    print('Example 3-1 = ', sol.Optimized(n))  # Expected 30
    
    n = 0
    print('Example 4 = ', sol.hammingWeight(n))  # Expected 0        print('Example 4 = ', sol.hammingWeight(n))  # Expected 0
    print('Example 4-1 = ', sol.Optimized(n))  # Expected 0

    n = n = 0xFFFFFFFF
    print('Example 5 = ', sol.hammingWeight(n))  # Expected 32
    print('Example 5-1 = ', sol.Optimized(n))  # Expected 32