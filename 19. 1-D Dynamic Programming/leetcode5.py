'''
5. Longest Palindromic Substring
Medium

Topics
Companies

Hint
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #s="babad"
        #b -> yes
        #ba -> no
        #bab -> yes
        #baba -> no
        #babad -> no
        if len(s) == 0:
            return ""
    
        def expand_around_center(s: str, left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest_palindrome = ""
        for i in range(len(s)):
            # Odd length palindromes
            odd_palindrome = expand_around_center(s, i, i)
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
            # Even length palindromes
            even_palindrome = expand_around_center(s, i, i + 1)
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome
        
        return longest_palindrome

    def DynamicProgramming(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        # 初始化DP表
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_length = 1

        # 所有长度为1的子串都是回文
        for i in range(n):
            dp[i][i] = True

        # 检查长度为2的子串
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2

        # 检查长度大于2的子串
        for length in range(3, n + 1):  # 子串的长度从3到n
            for i in range(n - length + 1):  # 子串起始位置
                j = i + length - 1  # 子串结束位置
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    start = i
                    max_length = length

        return s[start:start + max_length]

solution = Solution()

s = "babad"
print('Result1 = ', solution.longestPalindrome(s))

s = "cbbd"
print('Result2 = ', solution.longestPalindrome(s))
