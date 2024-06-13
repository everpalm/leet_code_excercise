'''
199. Binary Tree Right Side View
Medium

Topics
Companies
Given the root of a binary tree, imagine yourself standing on the right side
of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
 
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        queue = deque([root])
        right_view = []

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                # If it's the last node in the current level, add it to the result
                if i == level_length - 1:
                    right_view.append(node.val)
                # Add left and right children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return right_view


solution = Solution()

# Exampel1: Create the tree [1,2,3,null,5,null,4]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
print('Result1 = ', solution.rightSideView(root))  # Output: [1, 3, 4]

# Example2: Create the tree [1, null, 3]
root = TreeNode(1)
root.right = TreeNode(3)
print('Result2 = ', solution.rightSideView(root))  # Output: [1, 3]

# Example3: Create the tree []
print('Result3 = ', solution.rightSideView([]))  # Output: []
