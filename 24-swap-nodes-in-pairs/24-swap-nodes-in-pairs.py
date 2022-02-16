# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        
        node = head.next.next
        
        temp = head
        head = head.next
        head.next = temp

        head.next.next = self.swapPairs(node)
        return head