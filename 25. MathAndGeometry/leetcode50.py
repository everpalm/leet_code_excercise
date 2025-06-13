'''
50. Pow(x, n)
Medium

Topics
premium lock icon
Companies
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 
Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n

    def myPow_brute_force(self, x: float, n: int) -> float:
        # 处理特殊情况
        if n == 0:
            return 1.0
        
        result = 1.0
        power = abs(n)
        
        for _ in range(power):
            result *= x
        
        if n < 0:
            return 1 / result
        return result


    def myPow_optimal(self, x: float, n: int) -> float:
        def fast_pow(base: float, exponent: int) -> float:
            if exponent == 0:
                return 1.0
            
            half = fast_pow(base, exponent // 2)
            if exponent % 2 == 0:
                return half * half
            else:
                return half * half * base

        if n < 0:
            x = 1 / x
            n = -n
        return fast_pow(x, n)

    def myPow_advanced(self, x: float, n: int) -> float:
        N = abs(n)
        res = 1.0
        current_product = x  # 我們獨立出來，不動原始 x

        while N > 0:
            if N % 2 == 1:
                res *= current_product
            current_product *= current_product  # 這個值才真的會再被用到
            N //= 2

        return res if n >= 0 else 1 / res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow_brute_force(2.00000, 10))  # 应该输出 1024.00000
    print(solution.myPow_brute_force(2.10000, 3))   # 应该输出 9.26100
    print(solution.myPow_brute_force(2.00000, -2))  # 应该输出 0.25000
    
    print(solution.myPow_optimal(2.00000, 10))  # 应该输出 1024.00000
    print(solution.myPow_optimal(2.10000, 3))   # 应该输出 9.26100
    print(solution.myPow_optimal(2.00000, -2))  # 应该输出 0.25000

    print(solution.myPow_advanced(2.00000, 10))  # 应该输出 1024.00000
    print(solution.myPow_advanced(2.10000, 3))   # 应该输出 9.26100
    print(solution.myPow_advanced(2.00000, -2))  # 应该输出 0.25000
    

