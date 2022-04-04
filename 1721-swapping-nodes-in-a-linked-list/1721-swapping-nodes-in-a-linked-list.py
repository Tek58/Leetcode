# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head
        for i in range(k-1):
            fast = fast.next
        
        slow = head
        firstVal = fast
        while fast.next:
            slow, fast = slow.next, fast.next
        
        firstVal.val, slow.val = slow.val, firstVal.val
        return head
            
        
        
        
        
