'''
1143. Longest Common Subsequence
Medium

Topics
Companies

Hint
Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing the relative order
of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both
strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
<<<<<<< HEAD

text1 = abc
text2 = aac
==> common subsequence is ac
i = 0, j = 0
text1[0] = a
text2[0] = a

i = 1, j = 1
text1[1] = b
text2[1] = a

i = 1, j = 2
text1[1] = b
text2[2] = c

i = 2, j = 1
text1[2] = c
text2[1] = a 

=======
>>>>>>> ba89f9d (CLI-87-Longest-Common-Subsequence)
'''
class Solution:
    def dynamic_programming(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # 創建 dp 陣列
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 填充 dp 陣列
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]  # 返回最長公共子序列的長度
    
    def brute_force(self, text1: str, text2: str) -> int:
        def dfs(i, j):
        # 基礎情況：如果任一字串的索引超出範圍
            if i >= len(text1) or j >= len(text2):
                return 0
            
            # 如果字符相等，則計算下一個字符
            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)
            else:
                # 否則，考慮跳過一個字符
                return max(dfs(i + 1, j), dfs(i, j + 1))

        return dfs(0, 0)  # 從兩個字串的起始位置開始

# 測試
solution = Solution()
print(solution.dynamic_programming("abcde", "ace"))  # 輸出: 3
print(solution.dynamic_programming("abc", "abc"))    # 輸出: 3
print(solution.dynamic_programming("abc", "def"))    # 輸出: 0
print(solution.brute_force("abcde", "ace"))  # 輸出: 3
print(solution.brute_force("abc", "abc"))    # 輸出: 3
print(solution.brute_force("abc", "def"))    # 輸出: 0