'''
110. Balanced Binary Tree
Easy

Topics
Companies
Given a binary tree, determine if it is 
height-balanced
.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node):
            if not node:
                return 0, True
            
            left_height, left_balanced = check_height(node.left)
            right_height, right_balanced = check_height(node.right)
            
            current_height = max(left_height, right_height) + 1
            current_balanced = left_balanced and right_balanced \
                and abs(left_height - right_height) <= 1
        
            return current_height, current_balanced
    
        _, balanced = check_height(root)
        return balanced
    

node1 = TreeNode(15, None, None)
node2 = TreeNode(7, None, None)
node3 = TreeNode(20, node1, node2)
node4 = TreeNode(9, None, None)
node5 = TreeNode(3, node4, node3)

my_solution = Solution()
print('Result1 = ', my_solution.isBalanced(node5))

# root = [1,2,2,3,3,null,null,4,4]
node1 = TreeNode(4, None, None)
node2 = TreeNode(4, None, None)
node3 = TreeNode(3, node1, node2)
node4 = TreeNode(3, None, None)
node5 = TreeNode(2, node3, node4)
node6 = TreeNode(2, None, None)
node7 = TreeNode(1, node5, node6)
print('Result2 = ', my_solution.isBalanced(node7))
print('Result3 = ', my_solution.isBalanced(None))

