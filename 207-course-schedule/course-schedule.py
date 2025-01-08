from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)
        
        visited = [False] * numCourses
        rec_stack = [False] * numCourses

        def is_cyclic(node):
            visited[node] = True
            rec_stack[node] = True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if is_cyclic(neighbor):
                        return True
                elif rec_stack[neighbor]:
                    return True

            rec_stack[node] = False
            return False

        for course in range(numCourses):
            if not visited[course]:
                if is_cyclic(course):
                    return False  # Cycle detected

        return True