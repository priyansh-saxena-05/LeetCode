from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Initialize the queue and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # Directions for adjacent cells
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes = 0
        
        # Perform BFS
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # Check bounds and if the cell has a fresh orange
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  # Mark it as rotten
                        fresh_count -= 1
                        queue.append((nx, ny))
            minutes += 1
        
        # If fresh oranges remain, return -1
        return minutes if fresh_count == 0 else -1