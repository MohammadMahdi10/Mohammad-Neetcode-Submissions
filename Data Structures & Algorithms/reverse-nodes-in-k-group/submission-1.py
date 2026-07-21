# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        length = 0
        while current != None:
            length += 1
            current = current.next
        div = length // k
        
        dummy = ListNode(0, head)
        previousTail = dummy
        current = head

        while div > 0:
            groupTail = current
            prev = None

            for _ in range(k):
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt

            previousTail.next = prev
            groupTail.next = current

            previousTail = groupTail
            div -= 1

        return dummy.next