'''
846. Hand of Straights
Medium

Topics
Companies
Alice has some number of cards and she wants to rearrange the cards into
groups so that each group is of size groupSize, and consists of groupSize
consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card
and an integer groupSize, return true if she can rearrange the cards, or false
otherwise.

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

 
Constraints:
1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
'''
from collections import Counter

class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        
        while count:
            min_val = min(count)
            for i in range(min_val, min_val + groupSize):
                if count[i] == 0:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    del count[i]
        
        return True

# Example usage:
solution = Solution()

hand1 = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize1 = 3
print(solution.isNStraightHand(hand1, groupSize1))  # Output: True

hand2 = [1, 2, 3, 4, 5]
groupSize2 = 4
print(solution.isNStraightHand(hand2, groupSize2))  # Output: False
