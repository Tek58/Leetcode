# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        answer = head
        carry = 0
        current = 0
        while l1 or l2 or carry:
            num1 = 0
            num2 = 0
            if l1:
                num1 = l1.val
                l1= l1.next
            if l2:
                num2 = l2.val
                l2 = l2.next
            ans = num1 + num2 + carry
            current = ans %10
            head.next = ListNode(current)
            carry = ans // 10
            head = head.next
        return answer.next