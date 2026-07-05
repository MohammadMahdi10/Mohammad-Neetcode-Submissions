# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = self.reverse(head)
        
        prev = None
        current = head
        nxt = current
        index = 1

        while index < n:
            prev = nxt
            nxt = nxt.next
            index += 1

        if index == 1:
            current = current.next
        else:
            prev.next = nxt.next
            
        head = self.reverse(current)
        return head

    def reverse(self, head):        
        current = head
        prev = None

        while current != None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        
        head = prev
        return head