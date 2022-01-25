class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3 or A[0]>=A[1]:
            return False
			
        uphill = True
        
        for i in range(1,len(A)):
            if uphill:
                if A[i-1]>=A[i]:
                    uphill = False
            if not uphill:
                if A[i-1]<=A[i]:
                    return False
        return not uphill
    
            
            