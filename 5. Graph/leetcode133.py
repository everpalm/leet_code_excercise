'''
133. Clone Graph
Medium

Topics
Companies
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

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists
of only one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
 
Constraints:
The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given
node.
'''
class Node:
    def __init__(self, val: int = 0, neighbors: list = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None

        # Dictionary to store the cloned nodes
        cloned_nodes = {}

        def dfs(node: Node) -> Node:
            # If the node is already cloned, return the cloned node
            if node in cloned_nodes:
                return cloned_nodes[node]

            # Clone the node
            clone = Node(node.val)
            cloned_nodes[node] = clone

            # Clone all the neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone

        return dfs(node)

# Helper function to build a graph from an adjacency list
def build_graph(adjList):
    if not adjList:
        return None
    
    nodes = [Node(i + 1) for i in range(len(adjList))]
    
    for i, neighbors in enumerate(adjList):
        for neighbor in neighbors:
            nodes[i].neighbors.append(nodes[neighbor - 1])
    
    return nodes[0]

# Helper function to convert graph to adjacency list for easy comparison
def graph_to_adjList(node: Node):
    if not node:
        return []
    
    adjList = []
    visited = set()
    stack = [node]
    
    while stack:
        n = stack.pop()
        if n.val - 1 >= len(adjList):
            adjList.extend([[] for _ in range(n.val - len(adjList))])
        adjList[n.val - 1] = [neighbor.val for neighbor in n.neighbors]
        
        for neighbor in n.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    
    return adjList

# Example test cases
adjList1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
adjList2 = [[]]
adjList3 = []

graph1 = build_graph(adjList1)
graph2 = build_graph(adjList2)
graph3 = build_graph(adjList3)

solution = Solution()

cloned_graph1 = solution.cloneGraph(graph1)
cloned_graph2 = solution.cloneGraph(graph2)
cloned_graph3 = solution.cloneGraph(graph3)

print(graph_to_adjList(cloned_graph1))  # Should output: [[2, 4], [1, 3], [2, 4], [1, 3]]
print(graph_to_adjList(cloned_graph2))  # Should output: [[]]
print(graph_to_adjList(cloned_graph3))  # Should output: []
