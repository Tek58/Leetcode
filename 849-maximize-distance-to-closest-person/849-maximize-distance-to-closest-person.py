class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        first = 0
        second = 1
        res = 0
        while second < len(seats):
            if seats[second] != 1:
                second += 1
            else:
                if first == 0 and seats[first] != 1:
                    res = max(res, second)
                else:
                    val = (second - first)//2
                    res = max(res, val)
                first = second
                second += 1
                
        if seats[second-1] != len(seats)-1  and seats[second-1] != 1:
            res = max(res, (len(seats) -1 - first))
            
        return res
                
            
            