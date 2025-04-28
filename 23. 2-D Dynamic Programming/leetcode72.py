'''
72. Edit Distance
Medium

Topics
Companies
Given two strings word1 and word2, return the minimum number of operations
required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 
Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
'''
from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        '''
        func name: dfs
        args:   i is index of word1
                j is index of word2
        return: minimum number operations
        '''
        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i == n1:
                return n2 - j  # All insertion, (n2 - j) times
            if j == n2:
                return n1 - i  # All insertion, (n1 - i) times
            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                return 1 + min(
                    dfs(i, j + 1),     # 插入
                    dfs(i + 1, j),     # 刪除
                    dfs(i + 1, j + 1)  # 替換
                )

        return dfs(0, 0)
    
    def dynamic_programming(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1 + 1):
            dp[i][0] = i
        for j in range(n2 + 1):
            dp[0][j] = j
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    )
        return dp[n1][n2]
    
if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    sol = Solution()
    print("Example 1 = ", sol.minDistance(word1, word2))  #Expected 3
    print("Example 1-1 = ", sol.dynamic_programming(word1, word2))  #Expected 3

    word1 = "intention"
    word2 = "execution"
    sol = Solution()
    print("Example 2 = ", sol.minDistance(word1, word2))  #Expected 5
    print("Example 2-1 = ", sol.dynamic_programming(word1, word2))  #Expected 5


