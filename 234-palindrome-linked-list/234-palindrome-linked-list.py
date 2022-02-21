# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        #know where the middle of the linkedlist will be
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse the second half 
        # second = slow.next
        prev  = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        first , second = head, prev
        while second:
            if first.val != second.val:
                return False
            first, second = first.next, second.next
        
        return True
        
        
        