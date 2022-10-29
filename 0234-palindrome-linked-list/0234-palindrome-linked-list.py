# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = temp = head
        while fast and fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
            temp = slow
            slow = slow.next
        
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        while prev:
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next
        
        return True
            
            
            
        