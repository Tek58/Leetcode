class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        memo = set()
        final = (1 << len(graph)) - 1
        res = [(i, 1 << i) for i in range(len(graph))]
        steps =  0
        while True:
            new = []
            for node, state in res:
                if state == final: return steps
                for v in graph[node]:
                    if (state | 1 << v, v) not in memo:
                        new.append((v, state | 1 << v))
                        memo.add((state | 1 << v, v))
            res = new
            steps += 1