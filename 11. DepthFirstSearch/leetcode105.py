'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

Topics
Companies
Given two integer arrays preorder and inorder where preorder is the preorder
traversal of a binary tree and inorder is the inorder traversal of the same
tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
 
Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        # The first element in preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        print('root.val = ', root.val)
        
        # Find the root in inorder to separate left and right subtrees
        mid = inorder.index(root_val)
        print('mid = ', mid)
        print('preorder[1:mid+1] = ', preorder[1:mid+1])
        print('inorder[:mid] = ', inorder[:mid])
        # Recursively build the left and right subtree
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root

# Example usage:
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
solution = Solution()
root = solution.buildTree(preorder, inorder)
# print('Result = ', solution.buildTree(preorder, inorder))
# Function to print the tree in level order to verify the solution
def printLevelOrder(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level = []
        next_queue = []
        for node in queue:
            if node:
                level.append(node.val)
                next_queue.append(node.left)
                next_queue.append(node.right)
            else:
                level.append(None)
        
        if any(node is not None for node in next_queue):  # Prevent adding levels with only None
            queue = next_queue
            result.append(level)
        else:
            break
    
    return result

print(printLevelOrder(root))
