class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        queue=deque([])
        n = len(dominoes)
        dominoes = list(dominoes)
        
        for i in range(len(dominoes)):
            if dominoes[i]!='.':
                queue.append((i, dominoes[i]))
        
        while queue:
            effect = {}
            for i in range(len(queue)):
                dom = queue.popleft()
                if (dom[0]==n-1 and dom[1]=='R') or (dom[0]==0 and dom[1]=='L'):
                    continue
                else:
                    j = dom[0]-1 if dom[1]=='L' else dom[0]+1
                    if dominoes[j]=='.':
                        if j in effect:
                            del effect[j]
                        else:
                            effect[j]=dom[1]
                    else:
                        pass
            for key in effect:
                dominoes[key]=effect[key]
                queue.append((key, effect[key]))
                
        return ''.join(dominoes)