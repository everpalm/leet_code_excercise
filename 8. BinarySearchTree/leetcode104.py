'''
104. Maximum Depth of Binary Tree
Easy

Topics
Companies
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
 

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
    

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Create an instance of Solution
solution = Solution()

# Calculate the maximum depth
depth = solution.maxDepth(root)
print('Result1 = ', depth)  # Output: 3

root = TreeNode(1)
root.right = TreeNode(2)
depth = solution.maxDepth(root)
print('Result2 = ', depth) # Output: 2