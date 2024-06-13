'''
235. Lowest Common Ancestor of a Binary Search Tree
Medium

Topics
Companies
Given a binary search tree (BST), find the lowest common ancestor (LCA) node
of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes p and q as the lowest node in T that has both p
and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2
 
Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Start from the root node
        current = root
        
        while current:
            # If both p and q are smaller than current, move to the left child
            if p.val < current.val and q.val < current.val:
                current = current.left
            # If both p and q are larger than current, move to the right child
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                # We have found the split point, i.e., the LCA node
                return current

# Example usage:
# Construct the BST as in the examples provided
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = root.left # Node 2
q = root.right # Node 8

# Create an instance of Solution
solution = Solution()

# Find LCA
lca = solution.lowestCommonAncestor(root, p, q)
print('Result1 = ', lca.val) # Output should be 6

# Another example:
p = root.left # Node 2
q = root.left.right # Node 4

# Find LCA
lca = solution.lowestCommonAncestor(root, p, q)
print('Result2 = ', lca.val) # Output should be 2

root = p = TreeNode(2)
root.left = q = TreeNode(1)

# Find LCA
lca = solution.lowestCommonAncestor(root, p, q)
print('Result3 = ', lca.val) # Output should be 2