class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colored = defaultdict(list)
        for i in range(len(graph)):
            if i not in colored and graph[i]:
                colored[i] = 1
                queue = collections.deque([i])
                while queue:
                    curr = queue.popleft()
                    for nb in graph[curr]:
                        if nb not in colored:
                            colored[nb] = -colored[curr]
                            queue.append(nb)
                        elif colored[nb] == colored[curr]:
                            return False
        return True