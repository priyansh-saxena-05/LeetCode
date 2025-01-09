class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return
            # Mark the cell as visited
            grid[i][j] = 0
            # Explore all directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Eliminate all cells connected to the boundaries
        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0 or i == n-1 or j == m-1) and grid[i][j] == 1:
                    dfs(i, j)

        # Count the remaining 1s
        return sum(grid[i][j] == 1 for i in range(n) for j in range(m))
