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
    def startWithPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]

        for i in range(1, len(strs)):
            count = 0    
            length = min(len(strs[i]), len(prefix))

            for j in range(length):
                if strs[i][j] == prefix[j]:
                    count += 1
                else:
                    break

            prefix = strs[i][:count]

            if prefix == "":
                break

        return prefix
    
    def vertical_scanning(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # 找到最短字串的長度
        min_len = min(len(s) for s in strs)
        
        # 遍歷到最短長度
        for i in range(min_len):
            # 獲取第一個字串當前位置的字符
            current_char = strs[0][i]
            
            # 檢查其他字串的相同位置
            for s in strs[1:]:
                if s[i] != current_char:
                    return strs[0][:i]
        
        # 如果所有字符都匹配，返回最短字串
        return strs[0][:min_len]


sol = Solution()

strs = ["flower","flow","flight"]

print("Example 1 = ", sol.longestCommonPrefix(strs))  # Expected = "fl"
print("Example 1-1 = ", sol.vertical_scanning(strs))
print("Example 1-2 = ", sol.startWithPrefix(strs))

strs = ["dog","racecar","car"]

print("Example 2 = ", sol.longestCommonPrefix(strs))  # Expected = ""
print("Example 2-1 = ", sol.vertical_scanning(strs))
print("Example 2-2 = ", sol.startWithPrefix(strs))

strs = ["ab","a"]

print("Example 3 = ", sol.longestCommonPrefix(strs))  # Expected = "a"
print("Example 3-1 = ", sol.vertical_scanning(strs))
print("Example 3-2 = ", sol.startWithPrefix(strs))

strs = ["abc","abc", "abc"]

print("Example 4 = ", sol.longestCommonPrefix(strs))  # Expected = "abc"
print("Example 4-1 = ", sol.vertical_scanning(strs))
print("Example 4-2 = ", sol.startWithPrefix(strs))

strs = ["abc"]

print("Example 5 = ", sol.longestCommonPrefix(strs))  # Expected = "abc"
print("Example 5-1 = ", sol.vertical_scanning(strs))
print("Example 5-2 = ", sol.startWithPrefix(strs))

strs = [""]

print("Example 6 = ", sol.longestCommonPrefix(strs))  # Expected = "abc"
print("Example 6-1 = ", sol.vertical_scanning(strs))
print("Example 6-2 = ", sol.startWithPrefix(strs))

strs = ["abc", ""]

print("Example 7 = ", sol.longestCommonPrefix(strs))  # Expected = "abc"
print("Example 7-1 = ", sol.vertical_scanning(strs))
print("Example 7-2 = ", sol.startWithPrefix(strs))