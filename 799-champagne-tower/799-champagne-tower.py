class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        res = [poured]
        for i in range(query_row):
            newwStore = [0] * (len(res) + 1)
            for i in range(len(res)):
                pour = (res[i] - 1)/2
                if pour > 0:
                    newwStore[i] += pour
                    newwStore[i+1] += pour
            
            res = newwStore
                    
        return min(1, res[query_glass])