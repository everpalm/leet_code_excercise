'''
787. Cheapest Flights Within K Stops
Medium

Topics
Companies
There are n cities connected by some number of flights. You are given an array
flights where flights[i] = [fromi, toi, pricei] indicates that there is a
flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price
from src to dst with at most k stops. If there is no such route, return -1.

Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has
cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because
it uses 2 stops.

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k =
1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has
cost 100 + 100 = 200.

Example 3:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k =
0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost
500.
 

Constraints:
1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
'''
from collections import defaultdict
from typing import List
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int,
                          dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # 記錄到達每個節點的最小成本和最小步數
        costs = [[float('inf')] * (k + 2) for _ in range(n)]
        
        pq = [(0, src, k + 1)]  # (cost, node, stops)
        
        while pq:
            cost, node, stops = heapq.heappop(pq)
            
            if node == dst:
                return cost
            
            if stops > 0:
                for neighbor, price in graph[node]:
                    new_cost = cost + price
                    if new_cost < costs[neighbor][stops - 1]:
                        costs[neighbor][stops - 1] = new_cost
                        heapq.heappush(pq, (new_cost, neighbor, stops - 1))
        
        return -1
    
    def dfs_find(self, n: int, flights: List[List[int]], src: int,
                    dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # 暴力解法：使用DFS遍歷所有路徑
        def dfs(node, stops, cost, visited):
            if stops < 0:  # 超過最大步數
                return float('inf')
            if node == dst:  # 到達目的地
                return cost
            
            min_cost = float('inf')
            for neighbor, price in graph[node]:
                if neighbor not in visited:  # 確保不重複訪問
                    visited.add(neighbor)
                    new_cost = dfs(neighbor, stops - 1, cost + price, visited)
                    min_cost = min(min_cost, new_cost)
                    visited.remove(neighbor)  # 回溯
            return min_cost
        
        result = dfs(src, k + 1, 0, {src})  # 初始化已訪問節點，步數加1
        return result if result != float('inf') else -1

    def bfs_find(self, n: int, flights: List[List[int]], src: int,
                 dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # 使用BFS遍歷所有路徑
        from collections import deque
        
        queue = deque([(src, 0, k + 1)])  # (node, cost, stops)
        min_cost = float('inf')
        
        while queue:
            node, cost, stops = queue.popleft()
            
            if node == dst:
                min_cost = min(min_cost, cost)
            
            if stops > 0:
                for neighbor, price in graph[node]:
                    new_cost = cost + price
                    queue.append((neighbor, new_cost, stops - 1))
        
        return min_cost if min_cost != float('inf') else -1

# Example usage:
sol = Solution()
# print(sol.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))  # Output: 700
# print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))  # Output: 200
# print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))  # Output: 500

print(sol.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))  # Output: 700
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))  # Output: 200
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))  # Output: 500

print(sol.bfs_find(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))  # Output: 700
print(sol.bfs_find(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))  # Output: 200
print(sol.bfs_find(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))  # Output: 500

print(sol.bfs_find(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))  # Output: 700
print(sol.bfs_find(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))  # Output: 200
print(sol.bfs_find(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))  # Output: 500