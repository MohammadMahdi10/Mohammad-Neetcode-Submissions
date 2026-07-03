# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}

        index = -1
        current = head

        while current != None:
            if current not in seen:
                index += 1
                seen[current] = index 
            else:
                index = seen[current]
                return True
            
            current = current.next
        
        return False