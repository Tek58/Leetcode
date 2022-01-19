# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = defaultdict(int)
        while head:
            if head.next not in visited:
                visited[head] = head
            else:
                val = visited[head.next]
                return val
            head = head.next
        return None
            