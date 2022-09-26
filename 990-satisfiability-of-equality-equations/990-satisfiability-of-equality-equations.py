class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        leader = [i for i in range(26)]
        def find(x):
            if x == leader[x]:
                return x
            return find(leader[x])
        
        def union(x, y):
            xLeader = find(x)
            yLeader = find(y)
            leader[xLeader] = yLeader
            
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