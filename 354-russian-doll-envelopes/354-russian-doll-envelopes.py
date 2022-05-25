class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
            
        res = []
        for envelop in envelopes:
            if res and res[-1][0] < envelop[0] and res[-1][1] < envelop[1]: 
                res.append(envelop)
                continue

            for i in range(len(res)):
                if res[i][1] >= envelop[1]: 
                    res[i] = envelop
                    break
            else:
                res.append(envelop)
                
        return len(res)