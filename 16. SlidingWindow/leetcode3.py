'''
3. Longest Substring Without Repeating Characters
Solved
Medium

Topics
Companies

Hint
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # buffer = set()
        # counter = max_count = 0
        # for char in s:
        #     if char in buffer:
        #         counter = 1
        #     else:
        #         counter += 1
        #         buffer.add(char)
        #     max_count = max(max_count, counter)
        last_seen = {}
        start = 0
        max_length = 0
        for end in range(len(s)):
            # print(f's[{end}] = {s[end]}')
            if s[end] in last_seen and last_seen[s[end]] >= start:
                start = last_seen[s[end]] + 1
                print(f'{s[end]} start = ', start)
            last_seen[s[end]] = end
            print(f'last_seen[{s[end]}] = {last_seen[s[end]]}')
            max_length = max(max_length, end - start + 1)
        return max_length
    

my_solution = Solution()
s = "abcabcbb"
print(f'Result1 = {my_solution.lengthOfLongestSubstring(s)}')
s = "bbbbb"
print(f'Result2 = {my_solution.lengthOfLongestSubstring(s)}')
s = "pwwkew"
print(f'Result3 = {my_solution.lengthOfLongestSubstring(s)}')
s = "1"
print(f'Result4 = {my_solution.lengthOfLongestSubstring(s)}')