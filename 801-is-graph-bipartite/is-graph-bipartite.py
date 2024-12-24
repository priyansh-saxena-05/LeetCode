from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        for i in range(n):
            if color[i] == -1:
                queue = deque([i])
                color[i] = 0

                while queue:
                    node = queue.popleft()
                    for n_node in graph[node]:
                        if color[n_node] == -1:
                            color[n_node] = 1 - color[node]
                            queue.append(n_node)
                        elif color[n_node] == color[node]:
                            return False
        return True
