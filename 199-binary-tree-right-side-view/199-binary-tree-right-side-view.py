# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root] if root else []
        while stack:
            newStack = []
            result.append(stack[-1].val)
            for elem in stack:
                if elem.left: 
                    newStack.append(elem.left)
                if elem.right: 
                    newStack.append(elem.right)
            stack = newStack
        return result