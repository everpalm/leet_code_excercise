'''
261. Graph Valid Tree

Medium

Company

Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge
is a pair of nodes), write a function to check whether these edges make up a
valid tree.

Example 1:
n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]

Example 2:
n = 5, 
edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]

Note: you can assume that no duplicate edges will appear in edges. Since all
edges are undirected,[0,1] is the same as [1,0] and thus will not appear
together in edges.
'''
class Solution:
    def valid_tree(self, n, edges):
        if not n:
            return True
        
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2) 
            adj[n2].append(n1)

        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True
        return dfs(0, -1) and n == len(visit)
            
solution = Solution()
# n = 5
# edges = [[0,1], [0,2], [0,3], [1,4]]
# print('Result1 = ', solution.valid_tree(n, edges))

n = 5
edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
print('Result2 = ', solution.valid_tree(n, edges))

#         if len(edges) != n - 1:
#             return False

#         # Union-Find data structure with path compression and union by rank
#         parent = list(range(n))
#         rank = [1] * n

#         def find(x):
#             if parent[x] != x:
#                 parent[x] = find(parent[x])
#             return parent[x]

#         def union(x, y):
#             rootX = find(x)
#             rootY = find(y)
#             if rootX != rootY:
#                 if rank[rootX] > rank[rootY]:
#                     parent[rootY] = rootX
#                 elif rank[rootX] < rank[rootY]:
#                     parent[rootX] = rootY
#                 else:
#                     parent[rootY] = rootX
#                     rank[rootX] += 1
#                 return True
#             return False

#         for u, v in edges:
#             if not union(u, v):
#                 return False
        
#         return True


# class UnionFind:
#     def __init__(self, size):
#         # 初始化每个元素的父节点为自身
#         self.parent = list(range(size))
#         self.rank = [1] * size  # 使用 rank 数组优化合并操作

#     def find(self, x):
#         # 路径压缩：将 x 的所有祖先节点直接连接到根节点
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self, x, y):
#         rootX = self.find(x)
#         rootY = self.find(y)

#         if rootX != rootY:
#             # 按秩合并：将较低秩的树合并到较高秩的树上
#             if self.rank[rootX] > self.rank[rootY]:
#                 self.parent[rootY] = rootX
#             elif self.rank[rootX] < self.rank[rootY]:
#                 self.parent[rootX] = rootY
#             else:
#                 self.parent[rootY] = rootX
#                 self.rank[rootX] += 1
#             return True
#         return False

# Example 1
# n1 = 5
# edges1 = [[0,1], [0,2], [0,3], [1,4]]
# solution = Solution()
# print(solution.valid_tree(n1, edges1))  # Should print True

# # Example 2
# n2 = 5
# edges2 = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# print(solution.valid_tree(n2, edges2))  # Should print False

# test = UnionFind(3)

# test_parent = test.find(1)
# print('test_parent = ', test_parent)
