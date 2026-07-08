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

        while curr1 and curr2:
            div = 0
            rem = 0

            sums = curr1.val + curr2.val
            if (sums) >= 10:
                div = sums // 10
                rem = sums - 10
                curr.next = ListNode(rem)
                curr = curr.next
                curr.next = ListNode(div)
                curr = curr.next
            else:
                curr.next = ListNode(sums)
                curr = curr.next
        
            curr1 = curr1.next
            curr2 = curr2.next

        return head.next