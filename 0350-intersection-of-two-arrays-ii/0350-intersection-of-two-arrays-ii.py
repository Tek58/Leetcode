class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        visited = set()
        res = []
        for num in nums2:
            if num in count1 and num not in visited:
                freq = min(count1[num], count2[num])
                for i in range(freq):
                    res.append(num)
            visited.add(num)
        return res
    
