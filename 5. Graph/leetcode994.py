'''
994. Rotting Oranges
Medium

Topics
Companies
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a
fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never
rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer
is just 0.
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
'''
from collections import deque

class Solution:
    def orangesRottingDFS(self, grid):
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        fresh_oranges = 0
        max_minutes = 0

        # Count fresh oranges and add rotten oranges to a list with their starting minute
        rotten_oranges = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    rotten_oranges.append((r, c, 0))

        # DFS function to rot adjacent fresh oranges
        def dfs(x, y, minutes):
            nonlocal max_minutes
            max_minutes = max(max_minutes, minutes)
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    dfs(nx, ny, minutes + 1)

        # Apply DFS starting from all initially rotten oranges
        for x, y, start_minutes in rotten_oranges:
            dfs(x, y, start_minutes)

        # Check if there are still fresh oranges left
        for row in grid:
            if 1 in row:
                return -1

        return max_minutes


    def orangesRottingBFS(self, grid):
        if not grid:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        
        # Initialize the queue with all rotten oranges and count the fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        # If there are no fresh oranges, return 0 as no time is needed
        if fresh_oranges == 0:
            return 0
        
        minutes_passed = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Perform BFS
        while queue and fresh_oranges > 0:
            minutes_passed += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_oranges -= 1
                        queue.append((nx, ny))
        
        # If there are still fresh oranges left, return -1
        return minutes_passed if fresh_oranges == 0 else -1
    
# Example usage
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
solution = Solution()
# print(solution.orangesRottingDFS(grid))  # Output: 4
print(solution.orangesRottingBFS(grid))  # Output: 4