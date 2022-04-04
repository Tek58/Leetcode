# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        store = []
        while head:
            store.append(head.val)
            head = head.next
        
        store[k-1], store[-k] = store[-k], store[k-1]
        dummy = ListNode()
        dummyNode = dummy
        for i in store:
            curr = ListNode(i)
            dummyNode.next = curr
            dummyNode = dummyNode.next
        
        return dummy.next
        
        
        
