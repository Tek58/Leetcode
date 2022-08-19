class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        sequence = defaultdict(int)   
        uncheked = Counter(nums) 
        
        for num in nums:
            if ( not uncheked[num] ): 
                continue
                
            if (sequence[num - 1] > 0):
                sequence[num - 1] -= 1 
                sequence[num] += 1
                uncheked[num] -= 1
                
            else:
                if ( not uncheked[num + 1] or not uncheked[num + 2] ):
                    return False
                uncheked[num] -= 1
                uncheked[num + 1] -= 1
                uncheked[num + 2] -= 1
                sequence[num + 2] += 1
        
        return True