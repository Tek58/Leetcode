from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        sorted_list = SortedList()
        
        for i in range(len(nums)-1, -1, -1):
            curr = SortedList.bisect_left(sorted_list, nums[i])
            res.append(curr)
            sorted_list.add(nums[i])
        
        return reversed(res)