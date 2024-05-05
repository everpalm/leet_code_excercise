'''
567. Permutation in String

Medium

Topics
Companies

Hint
Given two strings s1 and s2, return true if s2 contains a permutation of s1,
or false otherwise.

In other words, return true if one of s1's permutations is the substring of
s2.

 
Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # left, right = 0, len(s1)
        # # print('left = ', left)
        # # print('right = ', right)
        # for left in range(len(s2)-right+1):
        #     # print('s2[left:right] = ', s2[left:right])
        #     if sorted(s2[left:right]) == sorted(s1):
        #         return True
        #     left += 1
        #     right += 1
        # return False

        len1, len2 = len(s1), len(s2)
        
        # If s1 is longer than s2, it's impossible for s2 to contain any permutation of s1
        if len1 > len2:
            return False

        # Frequency count of characters in s1 and the first window of s2
        count1 = Counter(s1)
        print('count1 = ', count1)
        count2 = Counter(s2[:len1])
        print('count2 = ', count2)

        # If the first window is a match
        if count1 == count2:
            return True
        
        # Start sliding the window
        for i in range(len1, len2):
            # Enter a new character to the window
            count2[s2[i]] += 1
            # Remove the character that is left behind as the window slides
            print(f'len1 = {len1}, i = {i}')
            count2[s2[i - len1]] -= 1
            # Remove the character count entirely if it goes to zero to keep the count2 clean
            if count2[s2[i - len1]] == 0:
                del count2[s2[i - len1]]
            # Check if after the slide the windows match
            if count1 == count2:
                return True
        
        return False

# Comment out the following line before sending the file
# check_inclusion("ab", "eidbaooo")  # Example 1, should return True
# check_inclusion("ab", "eidboaoo")  # Example 2, should return False


my_solution = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(f'Result1 = {my_solution.checkInclusion(s1, s2)}')

s1 = "ab"
s2 = "eidboaoo"
print(f'Result2 = {my_solution.checkInclusion(s1, s2)}')

s1 = "ab"
s2 = "ab"
print(f'Result3 = {my_solution.checkInclusion(s1, s2)}')

s1 = "eidboaoo"
s2 = "ab"
print(f'Result4 = {my_solution.checkInclusion(s1, s2)}')