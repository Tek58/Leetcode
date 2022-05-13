"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque([root])
        dummy = Node(-101)
        while queue:
            prev = dummy
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    prev.next = curr.left
                    prev = prev.next
                    
                if curr.right:
                    queue.append(curr.right)
                    prev.next = curr.right
                    prev = prev.next                
        return root