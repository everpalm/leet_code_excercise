'''
1584. Min Cost to Connect All Points
Medium

Topics
Companies

Hint
You are given an array points representing integer coordinates of some points
on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan
distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute
value of val.

Return the minimum cost to make all points connected. All points are connected
if there is exactly one simple path between any two points.

Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

Explanation: 
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 

Constraints:
1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
'''
# class Solution(object):
# # Iterate through the points and backtrack all the combinations of Manhattan distance
#     def find_min_distance(self, points):
#         min_distance = 0
#         num = len(points)

#         for i in range(num):
#             for j in range(i+1, num):
#                 manhattan_distance = abs(points[i][0] - points[j][0]) \
#                     + abs(points[j][1] - points[j][1])
#                 if i == 0:
#                     min_distance = manhattan_distance
#                 else:
#                     min_distance = min(min_distance, manhattan_distance)
#         return min_distance
    
# points = [[3,12],[-2,5],[-4,1]]
# sol = Solution()
# print("Result1 = ", sol.find_min_distance(points))
import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        
        # Priority queue to keep track of the minimum edge weight to a node not yet included in the MST
        pq = [(0, 0)]  # (cost, point_index)
        total_cost = 0
        in_mst = set()
        
        while len(in_mst) < n:
            cost, i = heapq.heappop(pq)
            if i in in_mst:
                continue
            in_mst.add(i)
            total_cost += cost
            
            # Check all points not in MST, and add the edge to the priority queue
            for j in range(n):
                if j not in in_mst:
                    manhattan_distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(pq, (manhattan_distance, j))
        
        return total_cost

    def brute_force(self, points):
        n = len(points)
        
        # Helper function to calculate the Manhattan distance between two points
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        # Generate all possible pairs of points
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((manhattan(points[i], points[j]), i, j))
        
        # Sort edges based on their distance
        edges.sort()
        
        # Union-Find (Disjoint Set) to detect cycles and manage connected components
        parent = list(range(n))
        # print(f'parent = {parent}')
        rank = [1] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                return True
            return False
        
        # Kruskal's algorithm to form MST, which is essentially the brute-force way in this context
        total_cost = 0
        for cost, i, j in edges:
            if union(i, j):
                total_cost += cost
                if sum(1 for p in range(n) if find(p) == find(0)) == n:
                    break
        
        return total_cost
# Example usage:
# points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# solution = Solution()
# print('Result1 = ', solution.minCostConnectPoints(points))  # Output: 20
# print('Result1_brute = ', solution.brute_force(points))  # Output: 20


points = [[3,12],[-2,5],[-4,1]]
solution = Solution()
# print('Result2 = ', solution.minCostConnectPoints(points))  # Output: 20
print('Result2_brute = ', solution.brute_force(points))  # Output: 20
