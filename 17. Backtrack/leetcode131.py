'''
131. Palindrome Partitioning
Medium

Topics
Companies
Given a string s, partition s such that every substring of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
 

Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
'''
from typing import List


# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         result = []
#         def dfs(start, path):
#             sorted_path = sorted(path)
#             if sorted_path == path:
#                 result.append(path)
#             for i in range(start, len(s)):
#                 dfs(i + 1, path + [s[i]])
#         dfs(0, [])
#         return result


class Solution:
    def partition(self, s):
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(start + len(substring), path)
                    path.pop()

        result = []
        backtrack(0, [])
        return result

# 测试用例
sol = Solution()
print(sol.partition("aab"))  # Output: [["a","a","b"],["aa","b"]]
# print(sol.partition("a"))    # Output: [["a"]]
