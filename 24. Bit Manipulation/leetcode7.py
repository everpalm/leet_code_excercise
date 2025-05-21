'''
7. Reverse Integer
Solved
Medium

Topics
Companies
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range
[-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers
(signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
 
Constraints:
-231 <= x <= 231 - 1
'''
class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        if str_x.startswith("-"):
            str_x = str_x[:0:-1]
            str_x = "-" + str_x
        else:
            str_x = str_x[::-1]
        res = int(str_x)
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res
    
    def popPush(self, x: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            # 在推入前做溢位检查
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and pop > INT_MAX % 10):
                return 0
            
            res = res * 10 + pop
        
        return sign * res
    
if __name__ == '__main__':
    x = 123
    sol = Solution()
    print('Example 1 = ', sol.reverse(x))  # Expected 321
    print('Example 1-1 = ', sol.popPush(x))  # Expected 321

    x = -123
    sol = Solution()
    print('Example 2 = ', sol.reverse(x))  # Expected -321
    print('Example 2-1 = ', sol.popPush(x))  # Expected -321

    x = 120
    sol = Solution()
    print('Example 3 = ', sol.reverse(x))  # Expected 21
    print('Example 3-1 = ', sol.popPush(x))  # Expected 21

    x = 0
    sol = Solution()
    print('Example 4 = ', sol.reverse(x))  # Expected 0
    print('Example 4-1 = ', sol.popPush(x))  # Expected 0

    x = -2**31 - 1
    sol = Solution()
    print('Example 5 = ', sol.reverse(x))  # Expected 0
    print('Example 5-1 = ', sol.popPush(x))  # Expected 0

    x = 2**31 + 1
    sol = Solution()
    print('Example 6 = ', sol.reverse(x))  # Expected 0
    print('Example 6-1 = ', sol.popPush(x))  # Expected 0
