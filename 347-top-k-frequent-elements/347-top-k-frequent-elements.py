class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [ [] for i in range(len(nums)+1) ]
        
        for key, val in count.items():
            freq[val].append(key)
        
        res = []
        for i in range(len(nums), 0, -1):
            if len(res) == k:
                return res
            elif freq[i]:
                res += freq[i]
                
        return res