class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        data = list(zip(plantTime, growTime))
        data.sort(key=lambda x: -x[1])
        
        res, start_time = 0, 0
        for plant, grow in data:
            start_time += plant
            res = max(res, start_time + grow)
        return res