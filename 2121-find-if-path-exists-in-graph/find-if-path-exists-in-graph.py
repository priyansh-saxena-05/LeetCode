from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)
        
        queue = deque()
    
        visited = [False] * n
        visited[source] = True
        queue.append(source)

        while queue:
            curr = queue.popleft()
            for neigh in graph[curr]:
                if not visited[neigh]:
                    visited[neigh] = True
                    queue.append(neigh)
            if curr == destination:
                return True
        return False