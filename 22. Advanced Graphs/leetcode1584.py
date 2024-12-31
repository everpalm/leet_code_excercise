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
        
        # 使用優先隊列來追蹤尚未包含在最小生成樹(MST)中的節點的最小邊權重
        pq = [(0, 0)]  # (成本, 點的索引)
        total_cost = 0
        in_mst = set()
        
        while len(in_mst) < n:
            cost, i = heapq.heappop(pq)
            if i in in_mst:
                continue
            in_mst.add(i)
            total_cost += cost
            
            # 檢查所有不在MST中的點，並將邊添加到優先隊列中
            for j in range(n):
                if j not in in_mst:
                    manhattan_distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(pq, (manhattan_distance, j))
        
        return total_cost

# 這段程式實現了Prim算法來解決最小生成樹問題。
# 它使用優先隊列來選擇最小權重的邊，逐步構建最小生成樹。
# 算法的主要步驟如下：
# 1. 初始化優先隊列，從第一個點開始。
# 2. 當還有點未加入MST時，重複以下步驟：
#    a. 從優先隊列中取出最小權重的邊。
#    b. 如果該邊連接的點已在MST中，跳過。
#    c. 否則，將該點加入MST，並更新總成本。
#    d. 對於新加入的點，計算它到所有未在MST中的點的距離，並加入優先隊列。
# 3. 返回總成本，即為連接所有點的最小成本。

    def kruskal_method(self, points):
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
    
    def brute_force1(self, points):
        n = len(points)

        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        
    
    def my_test(self, string):
        # return sum(1 for p in range(5) if p == 1 or p == 2)
        string = list(string)
        left, right = 0, len(string) - 1
        while left < right:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1
        return ''.join(string)
    
    def review_kruskal(self, points):
        n = len(points)
        def manhantan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs((p1[1] - p2[1]))

        edges = []
        for i in range(n):
            for j in range(i+1, n):
                edges.append(manhantan_distance((points[i], points[j]), i, j))

        edges.sort()

        parents = list(range(n))
        rank = [1] * n

        def find(x):
            if parents[x] != x:
                x = find(parents[x])
            return parents[x]
            
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if rank(root_x) > rank(root_y):
                    parents(root_y) = root_x
                elif rank(root_x) < rank(root_y):
                    parents(root_x) = root_y
                else:
                    parents(root_y) = root_x
                    rank[root_x] += 1
                return True
            return False
        
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


# points = [[3,12],[-2,5],[-4,1]]
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
solution = Solution()
print('minCostConnectPoints = ', solution.minCostConnectPoints(points))  # Output: 18
# print('kruskal_method = ', solution.kruskal_method(points))  # Output: 18

# print(solution.my_test('hello'))
# print('Result3_brute2 = ', solution.brute_force2(points))  # Output: 18
# print('test = ', solution.my_test())