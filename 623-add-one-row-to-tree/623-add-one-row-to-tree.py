# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new = TreeNode(val)
            new.left = root
            return new
        
        queue = collections.deque()
        queue.append(root)
        depth -= 1

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if depth == 1:
                    newLeft = TreeNode(val)
                    newRight = TreeNode(val)

                    if node.left:
                        newLeft.left = node.left
                    node.left = newLeft
                    
                    if node.right:
                        newRight.right = node.right
                    node.right = newRight
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            depth -= 1
        
        return root