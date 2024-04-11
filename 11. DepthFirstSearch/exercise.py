
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Dictionary to save the visited and cloned nodes
        visited = {}
        
        # Define the DFS function
        def dfs(node):
            if node in visited:
                return visited[node]
            
            # Clone the node and add it to the visited dictionary
            clone = Node(node.val)
            visited[node] = clone
            
            # Iterate over the neighbors to clone them
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node) if node else None
    

    # Case 1: 
    # Input: [[2,4],[1,3],[2,4],[1,3]]
    # Output: [[2,4],[1,3],[2,4],[1,3]]
    # Expected: [[2,4],[1,3],[2,4],[1,3]]

    # Case 2:
    # Input: [[]]
    # Output: [[]]
    # Expected: [[]]

    # Case 3: 
    # Input: []
    # Output: []
    # Expected: [] 
