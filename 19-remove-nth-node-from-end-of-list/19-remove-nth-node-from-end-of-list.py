# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        if count == 1:
            return None
        if count == n:
            head = head.next
            return head
        
        index = count - n
        prev = None
        curr = head
        local_count = 0
        while curr:
            if local_count == index:
                prev.next = curr.next
                break
            local_count += 1
            prev = curr
            curr = curr.next
        return head
        