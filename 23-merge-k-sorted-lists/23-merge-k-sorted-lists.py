# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = PriorityQueue()
        for i in range(len(lists)):
            if lists[i]:
                curr = (lists[i].val, i, lists[i].next)
                pq.put(curr)
        
        newNode = ListNode(0)
        curr = newNode
        while not pq.empty():
            val, index, node = pq.get()
            curr.next = ListNode(val)
            curr = curr.next
            if node:
                newVal = (node.val, index, node.next)
                pq.put(newVal)
        return newNode.next
