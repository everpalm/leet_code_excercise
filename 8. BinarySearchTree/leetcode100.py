'''100. Same Tree
Easy

Topics
Companies
Given the roots of two binary trees p and q, write a function to check if they
are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
 
Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Both nodes are None
        if not p and not q:
            return True
        # One node is None and the other is not
        if not p or not q:
            return False
        # Values of the nodes are different
        if p.val != q.val:
            return False
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Example usage:
my_solution = Solution()

# Define the trees for example 1
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))
print('Result1 = ', my_solution.isSameTree(p1, q1))

# Define the trees for example 2
p2 = TreeNode(1, TreeNode(2))
q2 = TreeNode(1, None, TreeNode(2))
print('Result2 = ', my_solution.isSameTree(p2, q2))

# Define the trees for example 3
p3 = TreeNode(1, TreeNode(2), TreeNode(1))
q3 = TreeNode(1, TreeNode(1), TreeNode(2))
# result3 = solution.isSameTree(p3, q3)
print('Result3 = ', my_solution.isSameTree(p3, q3))
# result1, result2, result3
