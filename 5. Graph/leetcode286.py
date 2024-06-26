'''
286. Wall and Gate

medium

company

You are given an m x n grid rooms initialized with these three possible values
.

-1 A wall or an obstacle.

0 A gate.

INF Infinity means an empty room. We use the value 2**31 - 1 = 2147483647 to
represent INF as you may assume that the distance to a gate is less than
2147483647.

Fill each empty room with the distance to its nearest gate. If it is
impossible to reach a gate, it should be filled with INF.

Example 1:
Input: rooms = [
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]
    ]
Output: [
    [3,-1,0,1],
    [2,2,1,-1],
    [1,-1,2,-1],
    [0,-1,3,4]
    ]

Example 2:
Input: rooms = [[-1]]
Output: [[-1]]

Constraints:
m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.
'''
from collections import deque

class Solution:
    def wallsAndGates(self, rooms):
        if not rooms:
            return
        
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        
        # Step 1: Initialize the queue with all gate positions
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        # Define directions for moving in the grid
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Step 2: Perform BFS from each gate
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == 2147483647:
                    rooms[nx][ny] = rooms[x][y] + 1
                    queue.append((nx, ny))

# Example usage
rooms1 = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]

solution = Solution()
solution.wallsAndGates(rooms1)
print(rooms1)  # Output should be the modified rooms grid with distances filled

rooms2 = [[-1]]
solution.wallsAndGates(rooms2)
print(rooms2)  # Output should be [[-1]]
