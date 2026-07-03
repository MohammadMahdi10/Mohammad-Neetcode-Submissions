# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        index = -1
        current = head

        while current != None:
            if current not in seen:
                seen.add(current)
            else:
                return True
            
            current = current.next
        
        return False