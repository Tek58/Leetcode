# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        numPaths = 0
        
        def dfs(node, pathSums):
            nonlocal numPaths
            if not node:
                return
            
            lastSum = pathSums[-1] 
            currSum = lastSum + node.val

            for prevSum in pathSums:
                diff = currSum - prevSum
                if diff == targetSum:
                    numPaths += 1
            
            pathSums.append(currSum)
            
            dfs(node.left, pathSums)
            if node.left:
                pathSums.pop()
                
            dfs(node.right, pathSums)
            if node.right:
                pathSums.pop()
            
        dfs(root, [0])
        return numPaths