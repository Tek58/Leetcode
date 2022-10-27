class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        res = [[1], [1,1]]
        
        for i in range(1,numRows-1):
            temp = [1]
            curr = res[i]
            for j in range(len(curr)-1):
                temp.append((curr[j] + curr[j+1]))
            temp.append(1)
            res.append(temp)
        
        return res
                
            