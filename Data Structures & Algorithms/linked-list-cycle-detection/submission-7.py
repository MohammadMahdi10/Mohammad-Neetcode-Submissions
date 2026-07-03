# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            index = -1
            return False
        
        index = 0
        slow = head
        fast = head

        while fast != None and fast.next != None:
            index += 1
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        index = -1
        return False