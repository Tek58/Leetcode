class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        stack = [intervals[0]]
        count = 0
        left = -1
        right = -1
        for i in intervals:
            if i[0] > left and i[1] > right:
                count += 1
                left = i[0]
            right = max(right, i[1])                
            
        
        return count
            
            
            