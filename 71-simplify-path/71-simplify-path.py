class Solution:
    def simplifyPath(self, path: str) -> str:
        absolute = [i for i in path.split("/") if i != "" if i != "."]
        canonical = []
        for i in absolute:
            if i == "..":
                if canonical:
                    canonical.pop()
            else:
                canonical.append(i)
            
        return "/" + "/".join(canonical)
        
        