# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = {}
        queue = deque([(root, 0)])
        
        while queue:
            new = []
            lvl_dict = {}
            for _ in range(len(queue)):
                node, pos = queue.popleft()
                
                lvl_dict[pos] = lvl_dict.get(pos, []) + [node.val]
                if node.left:
                    queue.append((node.left, pos - 1))
                
                if node.right:
                    queue.append((node.right, pos + 1))   
            
            for i in lvl_dict:
                if i in res:
                    res[i].extend(sorted(lvl_dict[i]))
                else:
                    res[i] = sorted(lvl_dict[i])
                    
        return [res[i] for i in sorted(res)]