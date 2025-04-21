'''
97. Interleaving String
Medium

Topics
Companies
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are
divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 +
t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = 
"aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other
string to obtain s3.

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
 
Constraints:
0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
 

Follow up: Could you solve it using only O(s2.length) additional memory space?
'''
from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        if n1 + n2 != n3:
            return False
        
        @lru_cache(None)
        def dfs(i: int, j: int) -> bool:
            k = i + j
            if k == n3:
                return i == n1 and j == n2
            
            valid = False
            if i < n1 and s1[i] == s3[k]:
                valid |= dfs(i + 1, j)
            if j < n2 and s2[j] == s3[k]:
                valid |= dfs(i, j + 1)
            return valid

        return dfs(0, 0)
    
    def dynamic_programming(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        if n1 + n2 != n3:
            return False
        
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True

        # 初始化第一列（只用 s2 組成）
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # 初始化第一欄（只用 s1 組成）
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
            
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                k = i + j - 1
                dp[i][j] = (
                    (dp[i - 1][j] and s1[i - 1] == s3[k]) or
                    (dp[i][j - 1] and s2[j - 1] == s3[k])
                )

        return dp[n1][n2] 

if __name__ == '__main__':
    sol = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print("Example1 = ", sol.isInterleave(s1, s2, s3))  # Expect True 
    print("Example1-1 = ", sol.dynamic_programming(s1, s2, s3))  # Expect True 

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    print("Example2 = ", sol.isInterleave(s1, s2, s3))  # Expect False 
    print("Example2-1 = ", sol.dynamic_programming(s1, s2, s3))  # Expect True 

    