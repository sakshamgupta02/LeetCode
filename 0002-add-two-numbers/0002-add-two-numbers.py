# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        head = l1
        prev = l1
        carry = 0
        while l1 or l2:

            sum_ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum_//10
            sum_ = sum_%10
            if l1:
                l1.val = sum_
                prev = l1
                l1 = l1.next

            else:
                newNode = ListNode(sum_, None)
                prev.next = newNode
                prev = prev.next

            if l2:
                l2 = l2.next

        if carry == 1:
            newNode = ListNode(carry, None)
            prev.next = newNode
            prev = prev.next

        return head        