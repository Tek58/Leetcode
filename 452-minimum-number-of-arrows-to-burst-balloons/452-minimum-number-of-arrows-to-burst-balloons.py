class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        # print(points)
        count = 1
        curr_intersection = points[0]
        for i in range(1,len(points)):
            curr = points[i]
            if curr_intersection[0] <= curr[0] <= curr_intersection[1] :
                curr_intersection = [max(curr[0], curr_intersection[0]), min(curr[1], curr_intersection[1])]   
                # print(curr_intersection)
            else:
                count += 1
                curr_intersection = curr
        
        return count
                
        