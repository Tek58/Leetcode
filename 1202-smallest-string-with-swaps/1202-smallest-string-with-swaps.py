class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:           
        n = len(s)
        adj_list = [[] for _ in range(n)]
        for i, j in pairs:
            adj_list[i].append(j)
            adj_list[j].append(i)
        visited = [0 for _ in range(n)]
        store = list(s)
        
        def dfs(i):
            visited[i] = 1
            component.append(i)
            for j in adj_list[i]:
                if not visited[j]:
                    dfs(j)
        
        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i)
                component.sort()
                chars = [store[k] for k in component]
                chars.sort()
                for i in range(len(component)):
                    store[component[i]] = chars[i]
        return ''.join(store)