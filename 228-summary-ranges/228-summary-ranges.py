class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        for num in nums:
            if result and result[-1][1] == num-1:
                result[-1][1] = num
            else:
                result.append([num,num])
                
        ranges = []
        for x, y in result:
            if x != y:
                ranges.append((str(x)+"->"+str(y)))
            else:
                ranges.append((str(x)))
                
        
        return ranges
                    
                