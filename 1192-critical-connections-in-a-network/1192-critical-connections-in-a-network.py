class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        for conn in connections:
            graph[conn[0]].append(conn[1])
            graph[conn[1]].append(conn[0])

        low = [0] * n
        res = []

        def dfs(node, parent, reachable):
            low[node] = reachable
            for neighbor in graph[node]:
                if parent != neighbor:
                    if not low[neighbor]:
                        dfs(neighbor, node, reachable+1)
                    if low[neighbor] > reachable:
                        res.append([node,neighbor])
                    else:
                        low[node] = min(low[neighbor], low[node])
                    
        dfs(0, -1, 1)
        return res