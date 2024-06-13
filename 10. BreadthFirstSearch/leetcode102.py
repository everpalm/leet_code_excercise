'''
102. Binary Tree Level Order Traversal
Medium

Topics
Companies
Given the root of a binary tree, return the level order traversal of its
nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 
Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Base case is a null node, return an empty list
        if not root:
            return []
        #Initialize result
        result = []
        #Create a queue to store result, the first element is the root
        queue = deque([root])
        print('queue[0].val = ', queue[0].val)
        #BFS: Iterate until the queue is empty
        while queue:
            level_size = len(queue)
            print('level_size = ', level_size)
            level_nodes = []
            #Iterate through the node levels(queue length)         
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                print('level_nodes = ', level_nodes)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)   
            result.append(level_nodes)
        return result

my_solution = Solution()        
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print('Result = ', my_solution.levelOrder(root))