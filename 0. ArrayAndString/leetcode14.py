'''
14. Longest Common Prefix
Solved
Easy

Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.
 
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
'''
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        str_length = len(strs)
        prefix = strs[0]

        for j in range(1, str_length):
            count = 0    
            length = min(len(strs[j]), len(prefix))

            for i in range(length):
                if strs[j][i] == prefix[i]:
                    count += 1
                else:
                    break
            prefix = strs[j][:count]
            if prefix == "":
                break
        return prefix
    

sol = Solution()

strs = ["flower","flow","flight"]

print("Example 1 = ", sol.longestCommonPrefix(strs))  # Expected = "fl"

strs = ["dog","racecar","car"]

print("Example 2 = ", sol.longestCommonPrefix(strs))  # Expected = ""

strs = ["ab","a"]

print("Example 3 = ", sol.longestCommonPrefix(strs))  # Expected = "a"