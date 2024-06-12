'''
543. Diameter of Binary Tree
Solved
Easy

Topics
Companies
Given the root of a binary tree, return the length of the diameter of the tree
.

The diameter of a binary tree is the length of the longest path between any
two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.

 

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
 
Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.diameter
    

my_solution = Solution()
node4 = TreeNode(4, None, None)
node5 = TreeNode(5, None, None)
node3 = TreeNode(3, None, None)
node2 = TreeNode(2, node4, node5)
node1 = TreeNode(1, node2, node3)
print('Result1 = ', my_solution.diameterOfBinaryTree(node1))

node2 = TreeNode(2, None, None)
node1 = TreeNode(1, node2, None)
print('Result2 = ', my_solution.diameterOfBinaryTree(node1))