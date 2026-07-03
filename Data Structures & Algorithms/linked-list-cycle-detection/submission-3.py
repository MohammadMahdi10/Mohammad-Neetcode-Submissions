# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            index = -1
            return head
        
        index = 0
        slow = head
        fast = head.next

        while slow != None and fast != None:
            if slow != fast:
                slow = slow.next
                fast = fast.next

                if fast != None:
                    fast = fast.next
                index += 1
            else:
                return True

        index = -1
        return False