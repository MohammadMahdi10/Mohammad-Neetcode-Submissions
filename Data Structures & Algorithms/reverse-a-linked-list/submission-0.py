# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        prev = None

        if current != None:
            nextNode = current.next
            
        while current != None:
            current.next = prev
            prev = current
            head = current
            current = nextNode
            if nextNode != None:
                nextNode = nextNode.next
        
        return head