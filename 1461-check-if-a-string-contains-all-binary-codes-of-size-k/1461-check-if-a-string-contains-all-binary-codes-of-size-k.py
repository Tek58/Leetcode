class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        res = 2**k
        visited = set()

        for i in range(k, len(s)+1):
            val = s[i-k:i]
            if val not in visited:
                visited.add(val)
                res -= 1
                if res == 0:
                    return True
        return False