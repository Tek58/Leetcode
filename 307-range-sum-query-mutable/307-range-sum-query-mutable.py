class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.total = sum(self.nums)
        

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        n = self.nums[index] 
        self.nums[index] = val
        self.total = self.total - n + val

        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        n1 = sum(self.nums[0:left])
        n2 = sum(self.nums[right+1:])
        return  self.total - n1 - n2
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
        