'''
647. Palindromic Substrings
Medium

Topics
Companies

Hint
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 
Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        palindromic_count = 0
        
        def expand_around_center(s: str, left: int, right: int) -> None:
            nonlocal palindromic_count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindromic_count += 1
                left -= 1
                right += 1
        
        for i in range(len(s)):
            # Odd length palindromes
            expand_around_center(s, i, i)
            # Even length palindromes
            expand_around_center(s, i, i + 1)
        
        return palindromic_count


class Solution2:
    def count_palindromic_substrings(self, s: str) -> int:
        n = len(s)
        count = 0

        for center in range(2 * n - 1):
            left = center // 2
            right = left + center % 2

            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count


solution = Solution()

s = "abc"
print('Result1 = ', solution.countSubstrings(s))
s = "aaa"
print('Result2 = ', solution.countSubstrings(s))

