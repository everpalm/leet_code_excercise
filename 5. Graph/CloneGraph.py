'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its
neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed).
For example, the first node with val == 1, the second node with val == 2, and
so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a
finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the
 copy of the given node as a reference to the cloned graph.

'''

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
            # If the node is already cloned, return the clone
            # for key, value in visited.items():
            for visited_node in visited:
                print('visited_node.val = ', visited_node.val)
                # print('value = ', value) 
            if node in visited:
                print('return to node ', visited[node].val)
                return visited[node]
            
            # Clone the node and add it to the visited dictionary
            clone = Node(node.val)
            visited[node] = clone
            print('clone.val = ', clone.val)
            # Iterate over the neighbors to clone them
            for neighbor in node.neighbors:
                print('neighbor.val = ', neighbor.val)
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node) if node else None
    
# Example creation of a graph and testing the cloneGraph function
# This part should be commented out before uploading or providing the code to the user
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

my_solution = Solution()
clone = my_solution.cloneGraph(node1)
# print('test1: ', clone.val)
# print('test2: ', clone.neighbors)

            