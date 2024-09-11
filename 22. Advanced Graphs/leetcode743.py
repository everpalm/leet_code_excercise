'''
743. Network Delay Time
Medium

Topics
Companies

Hint
You are given a network of n nodes, labeled from 1 to n. You are also given
times, a list of travel times as directed edges times[i] = (ui, vi, wi), where
ui is the source node, vi is the target node, and wi is the time it takes for
a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes
for all the n nodes to receive the signal. If it is impossible for all the n
nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 
Constraints:
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
'''
import heapq
import time
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        # Build the adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Min-heap to keep track of the minimum travel time to each node
        min_heap = [(0, k)]  # (time, node)
        # Dictionary to store the shortest time to each node
        shortest_time = {}
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            # If we've already visited this node, skip it
            if node in shortest_time:
                continue
            
            # Record the shortest time to reach this node
            shortest_time[node] = time
            
            # Update the time for each neighbor
            for neighbor, travel_time in graph[node]:
                if neighbor not in shortest_time:
                    heapq.heappush(min_heap, (time + travel_time, neighbor))
        
        # If all nodes are reachable, the maximum time will be our answer
        if len(shortest_time) == n:
            return max(shortest_time.values())
        
        # If not all nodes are reachable, return -1
        return -1

    def brute_force(self, times, n, k):
        dist = [float('inf')] * (n + 1)
        # 起始节点的距离为0
        dist[k] = 0
        
        # 进行n - 1次迭代（类似于Bellman-Ford算法的思路）
        for _ in range(n - 1):
            # 遍历所有边
            for u, v, w in times:
                # 如果从u到v的路径更短，则更新距离
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        # 找到所有节点的最短路径后，计算最远距离
        max_time = max(dist[1:])  # 忽略dist[0]，因为节点从1到n
        
        # 如果存在任何节点不可达，返回-1
        return max_time if max_time < float('inf') else -1
    
# Example usage:
sol = Solution()
# start_time = time.time()
# print(sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # Output: 2
# print(sol.networkDelayTime([[1, 2, 1]], 2, 1))  # Output: 1
# print(sol.networkDelayTime([[1, 2, 1]], 2, 2))  # Output: -1
# end_time = time.time()
# print("程序执行时间: {:.6f} 秒".format(end_time - start_time))

start_time = time.time()
print(sol.brute_force([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # Output: 2
print(sol.brute_force([[1, 2, 1]], 2, 1))  # Output: 1
print(sol.brute_force([[1, 2, 1]], 2, 2))  # Output: -1
end_time = time.time()
print("程序执行时间: {:.6f} 秒".format(end_time - start_time))

