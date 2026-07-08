# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        curr = head

        curr1 = l1
        curr2 = l2

        div = 0
        while curr1 and curr2:
            rem = 0

            sums = curr1.val + curr2.val
            if (sums) >= 10:
                rem = sums - 10
                curr.next = ListNode(rem + div)
                curr = curr.next
                div = sums // 10
            else:
                curr.next = ListNode(sums + div)
                curr = curr.next
                div = sums // 10
        
            curr1 = curr1.next
            curr2 = curr2.next
        
            a = None
            if curr1:
                a = curr1
            else:
                a = curr2

        while a:
            rem = 0
            sums = a.val + div
            if (sums) >= 10:
                div = 0
                rem = sums - 10
                curr.next = ListNode(rem + div)
                curr = curr.next
                div = sums // 10
            else:
                curr.next = ListNode(sums)
                curr = curr.next
                div = sums // 10
        
            a = a.next
        
        if div != 0:
            curr.next = ListNode(div)

        return head.next