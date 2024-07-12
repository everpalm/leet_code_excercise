'''
323. Number Connected Components In An Undirected Graph

Company
Medium

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
Return the number of connected components in the graph.

Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
 
Constraints:
1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
'''
from collections import defaultdict, deque
from typing import List

class Solution():
    def UnionFind(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2) 
            adj[n2].append(n1)

        visit = set()
        res = 0

        def dfs(curr):
            #Todo
            if curr in visit:
                return False
            
            visit.add(curr)
            for neighbor in adj[curr]:
                dfs(neighbor)
            return True

        for i in range(n):
            if dfs(i):
                res += 1
        return res


solution = Solution()
n = 5
edges = [[0,1],[1,2],[3,4]]
print('Result1 = ', solution.UnionFind(n, edges))

n = 5
edges = [[0,1],[1,2],[2,3],[3,4]]
print('Result2 = ', solution.UnionFind(n, edges))