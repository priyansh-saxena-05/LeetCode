from collections import deque, defaultdict
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = [0] * n
        ancestor = [set() for i in range(n)]
        
        # [0,1,2,3,4]
        for u, v in edges:
            graph[u].append(v)
            degree[v] += 1
        # [0]
        queue = deque([node for node in range(n) if degree[node] == 0])

        while queue:
            node = queue.popleft()
            # [0] --> 1, 2, 3
            for n_node in graph[node]:
                ancestor[n_node].update(ancestor[node])
                ancestor[n_node].add(node)
                degree[n_node] -= 1
                if degree[n_node] == 0:
                    queue.append(n_node)

        return [sorted(list(an)) for an in ancestor]


# 0 ->1 ->2 ->3
# 0--->3


# Time : O(N)
# Space: O(N)