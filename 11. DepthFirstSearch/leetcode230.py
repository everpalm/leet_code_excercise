'''
230. Kth Smallest Element in a BST
Solved
Medium

Topics
Companies

Hint
Given the root of a binary search tree, and an integer k, return the kth
smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 
Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 
Follow up: If the BST is modified often (i.e., we can do insert and delete
operations) and you need to find the kth smallest frequently, how would you
optimize?
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kth_smallest(self, root, k):
        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        left_count = count_nodes(root.left)
        
        if k <= left_count:
            return self.kth_smallest(root.left, k)
        elif k == left_count + 1:
            return root.val
        else:
            return self.kth_smallest(root.right, k - left_count - 1)

# 插入函数，用于构建示例树
def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# 示例用法:
# 构建例子1的BST: root = [3,1,4,null,2], k = 1
root1 = TreeNode(3)
root1 = insert(root1, 1)
root1 = insert(root1, 4)
root1 = insert(root1, 2)

sol = Solution()
k1 = 1
print('Result1 = ', sol.kth_smallest(root1, k1))  # 输出: 1

# 构建例子2的BST: root = [5,3,6,2,4,null,null,1], k = 3
root2 = TreeNode(5)
root2 = insert(root2, 3)
root2 = insert(root2, 6)
root2 = insert(root2, 2)
root2 = insert(root2, 4)
root2 = insert(root2, 1)

k2 = 3
print('Result2 = ', sol.kth_smallest(root2, k2))  # 输出: 3
