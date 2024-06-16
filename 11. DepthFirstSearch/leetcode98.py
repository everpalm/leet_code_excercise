'''
98. Validate Binary Search Tree
Medium

Topics
Companies
Given the root of a binary tree, determine if it is a valid binary search tree
(BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the
node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_valid_bst(self, root: TreeNode) -> bool:
        def validate(node, low=-float('inf'), high=float('inf')):
            # An empty tree is a valid BST
            if not node:
                return True
            # The current node's value must be within the range [low, high]
            if not (low < node.val < high):
                return False
            # Recursively validate the left and right subtrees
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root)

# Example usage:
# Constructing the tree [2, 1, 3]
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

# Constructing the tree [5, 1, 4, None, None, 3, 6]
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)

sol = Solution()
print('Result1 = ', sol.is_valid_bst(root1))  # Output: True
print('Result2 = ', sol.is_valid_bst(root2))  # Output: False
