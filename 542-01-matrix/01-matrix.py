from collections import deque

class Solution:
    def updateMatrix(self, mat):
        if not mat:
            return []

        rows, cols = len(mat), len(mat[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque()

        # Initialize the queue with all zeroes
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = float('inf')  # Set non-zero cells to a large number initially

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] > mat[r][c] + 1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
        
        return mat