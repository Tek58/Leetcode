class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        res = []
        for num in count2.keys():
            if num in count1:
                freq = min(count1[num], count2[num])
                for i in range(freq):
                    res.append(num)
        return res
    
