# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 1
        answer= [0]
        self.helper(root, depth, answer)
        return answer[0]
    
    def helper(self, node, depth, answer):
        if not node:
            return 
        if node.left == node.right:
            answer[0] = max(answer[0], depth)
        self.helper(node.left, depth+1, answer)
        self.helper(node.right, depth+1, answer)
        