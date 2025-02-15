class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i, j, area):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = dfs(i+1, j, area) + dfs(i, j+1, area) + dfs(i-1, j, area) + dfs(i, j-1, area) + 1
            return area
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j, 0))
        return ans