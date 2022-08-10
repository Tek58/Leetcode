# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        left = 0
        right = len(nums)-1
        return self.helper(left, right, nums)
    
    def helper(self, left, right, nums):
        if left > right:
            return None
        
        middle = (left + right)//2

        root = TreeNode(nums[middle])
        root.left = self.helper(left, middle-1, nums)
        root.right = self.helper(middle+1, right, nums)
        
        return root