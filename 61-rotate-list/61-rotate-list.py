# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        p=q=head
        l=1
        while p.next:
            p=p.next
            l+=1
        p.next=head
        k%=l
        for _ in range(l-k-1):
            q=q.next
        ans=q.next
        q.next=None
        return ans	