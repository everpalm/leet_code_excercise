'''
207. Course Schedule
Medium

Topics
Companies

Hint
There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i] = 
[ai, bi] indicates that you must take course bi first if you want to take
course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to
first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you
should also have finished course 1. So it is impossible.
 
Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
'''
from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 構建鄰接表
        graph = defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest)
        
        # 狀態：0 = 未訪問, 1 = 訪問中, 2 = 已訪問
        visited = [0] * numCourses
        
        def dfs(course):
            if visited[course] == 1:
                return False  # 發現環
            if visited[course] == 2:
                return True   # 已經檢查過這門課
            
            # 標記為訪問中
            visited[course] = 1
            
            # 訪問所有依賴這門課的課程
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            # 標記為已訪問
            visited[course] = 2
            return True
        
        # 檢查所有課程
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
    
# numCourses = 2
# prerequisites = [[1,0]]

solution = Solution()
# print('Result1 = ', solution.canFinish(numCourses, prerequisites))

# numCourses = 2
# prerequisites = [[1,0], [0, 1]]
# print('Result2 = ', solution.canFinish(numCourses, prerequisites))

numCourses = 4
prerequisites = [[0,1], [0, 2], [1, 3], [1, 4], [3, 4]]
print('Result3 = ', solution.canFinish(numCourses, prerequisites))