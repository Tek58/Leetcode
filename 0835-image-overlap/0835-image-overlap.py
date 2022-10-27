class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        store = defaultdict(int)
        arr1 = []
        arr2 = []
        for i in range(len(img1)):
            for j in range(len(img2)):
                if img1[i][j] == 1:
                    arr1.append((i, j))
                if img2[i][j] == 1:
                    arr2.append((i, j))
        
        res = 0
        for i in arr1:
            for j in arr2:
                diffIndex = (j[0] - i[0], j[1] - i[1])
                store[diffIndex] += 1
                res = max(res, store[diffIndex])
        
        return res