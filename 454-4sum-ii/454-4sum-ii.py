from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        container = defaultdict(int)
        counter = 0
        for i in nums1:
            for j in nums2:
                container[i+j] += 1
        
        for j in nums3:
            for k in nums4:
                val = -(j+k)
                if val in container:
                    counter += container[val]
                    
        return counter
        