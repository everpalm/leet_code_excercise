'''
202. Happy Number
Attempted
Easy

Topics
premium lock icon
Companies
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the
squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
 

Constraints:
1 <= n <= 231 - 1
'''
class Solution:
    def isHappy_brute_force(self, n: int) -> bool:
        def get_next(x):
            res = 0
            while x > 0:
                digit = x % 10
                res += digit * digit
                x //= 10
            return res

        seen = []
        while True:
            if n == 1:
                return True
            if n in seen:  # 進入循環
                return False
            seen.append(n)  # 暴力記錄所有曾經出現過的數字
            n = get_next(n)
    
    def isHappy_optimal(self, n: int) -> bool:
        def get_next(x):
            res = 0
            while x > 0:
                digit = x % 10
                res += digit * digit
                x //= 10
            return res

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.isHappy_brute_force(19))
    print(solution.isHappy_optimal(19))
    print(solution.isHappy_brute_force(2))
    print(solution.isHappy_optimal(2))