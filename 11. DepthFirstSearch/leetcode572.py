'''
572. Subtree of Another Tree
Easy

Topics
Companies

Hint
Given the roots of two binary trees root and subRoot, return true if there is
a subtree of root with the same structure and node values of subRoot and false
otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and
all of this node's descendants. The tree tree could also be considered as a
subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 
Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_identical(self, root: Optional[TreeNode],
    subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False

        left_same = self.is_identical(root.left, subRoot.left)
        right_same = self.is_identical(root.right, subRoot.right)
        return (left_same and right_same and (root.val == subRoot.val))

    def is_subtree(self, root, subRoot):
        if not root:
            return False
        if self.is_identical(root, subRoot):
            return True
        return self.is_subtree(root.left, subRoot) or self.is_subtree(root.right, subRoot)


root1 = TreeNode(3)
root1.left = TreeNode(4)
root1.right = TreeNode(5)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(2)
subRoot1 = TreeNode(4)
subRoot1.left = TreeNode(1)
subRoot1.right = TreeNode(2)

my_solution = Solution()
print('Result1 = ', my_solution.is_subtree(root1, subRoot1))

# # Example 2
root2 = TreeNode(3)
root2.left = TreeNode(4)
root2.right = TreeNode(5)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(2)
root2.left.right.left = TreeNode(0)
subRoot2 = TreeNode(4)
subRoot2.left = TreeNode(1)
subRoot2.right = TreeNode(2)

print('Result2 = ', my_solution.is_subtree(root2, subRoot2))
