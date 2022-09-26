class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        leader = [i for i in range(26)]
        rank = [1]*26
        
        def find(x):
            if x == leader[x]:
                return x
            leader[x] = find(leader[x])
            return leader[x]
        
        def union(x, y):
            xLeader = find(x)
            yLeader = find(y)
            xCount = rank[x]
            yCount = rank[y]
            if xCount > yCount:
                leader[xLeader] = yLeader
                rank[x] += rank[y]
            else:
                leader[yLeader] = xLeader
                rank[y] += rank[x]
            
        for equation in equations:
            x , y = equation[0], equation[-1]
            x , y = ord(x) - ord("a") , ord(y) - ord("a")
            if equation[1] == "=":
                union(x, y)
                
        for equation in equations:
            x , y = equation[0], equation[-1]
            x , y = ord(x) - ord("a") , ord(y) - ord("a")
            if equation[1] == "!" and find(x) == find(y):
                return False
        return True