class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1],[1,1]]
        if numRows == 1:
            return [result[0]]
        elif numRows == 2:
            return result
        for i in range(2, numRows):
            temp = [1]
            curr = result[i-1]
            for j in range(len(curr)-1):
                val = curr[j] + curr[j+1]
                temp.append(val)
            temp.append(1)
            result.append(temp)
        return result
            