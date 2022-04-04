class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points =  Counter(nums)
        prev , curr= 0, 0
        maxVal = max(points.keys()) + 1
        for value in range(maxVal):
            prev, curr = curr, max(prev + value * points[value], curr)
        return curr
    
