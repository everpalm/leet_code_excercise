'''
763. Partition Labels
Medium

Topics
Companies

Hint
You are given a string s. We want to partition the string into as many parts as
possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in
order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
'''
class Solution:
    def partitionLabels(self, s: str):
        # Step 1: Find the last occurrence of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        # Step 2: Iterate through the string to determine the partitions
        partitions = []
        start = 0
        end = 0
        
        for idx, char in enumerate(s):
            # Update the end pointer to the farthest last occurrence of the current character
            end = max(end, last_occurrence[char])
            
            # If the current index matches the end pointer, we found a partition
            if idx == end:
                # The size of the current partition is end - start + 1
                partitions.append(end - start + 1)
                # Move the start pointer to the next index after the current partition
                start = idx + 1
        
        return partitions

# Example usage:
solution = Solution()
s1 = "ababcbacadefegdehijhklij"
print(solution.partitionLabels(s1))  # Output: [9, 7, 8]

s2 = "eccbbbbdec"
print(solution.partitionLabels(s2))  # Output: [10]
