# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = []
        while head:
            sorted_list.append(head.val)
            head = head.next
        sorted_list.sort()
        dummy = ListNode()
        newNode = dummy
        for i in sorted_list:
            new = ListNode(i)
            newNode.next = new
            newNode = newNode.next
        
        return dummy.next