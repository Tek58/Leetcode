# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        leftIndex = left - 1
        rightIndex = right - 1
        
        while leftIndex <= rightIndex:
            res[leftIndex], res[rightIndex] = res[rightIndex], res[leftIndex]
            leftIndex += 1
            rightIndex -= 1
        
        # print(res)
        dummyNode = ListNode(res[0])
        head = dummyNode
        for i in range(1,len(res)):
            head.next = ListNode(res[i])
            head = head.next
        
        return dummyNode
            
            