class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        
        def build_graph(equations, values):
            def add_edge(first, second, value):
                if first in graph:
                    graph[first].append((second, value))
                else:
                    graph[first] = [(second, value)]
            
            for vertices, value in zip(equations, values):
                first, second = vertices
                add_edge(first, second, value)
                add_edge(second, first, 1/value)
        
        def find_path(query):
            first, second = query
            
            if first not in graph or second not in graph:
                return -1.0
                
            queue = deque([(first, 1.0)])
            visited = set()
            
            while queue:
                front, cur_product = queue.popleft()
                if front == second:
                    return cur_product
                visited.add(front)
                for neighbor, value in graph[front]:
                    if neighbor not in visited:
                        queue.append((neighbor, cur_product*value))
            
            return -1.0
        
        build_graph(equations, values)
        
        res = []
        for query in queries:
            currVal = find_path(query)
            res.append(currVal)
            
        return res