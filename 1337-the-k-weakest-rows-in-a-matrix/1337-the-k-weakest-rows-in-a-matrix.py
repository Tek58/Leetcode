class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        container = []
        result = []
        for i in range(len(mat)):
            container.append((sum(mat[i]), i))
        container.sort()
        
        for i in range(k):
            result.append(container[i][1])
        return result
