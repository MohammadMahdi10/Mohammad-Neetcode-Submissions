# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            current1 = list1
            current2 = list2

            if current1.val <= current2.val:
                head = current1
                current1 = current1.next
            else:
                head = current2
                current2 = current2.next

            newHead = head
            while current1 != None and current2 != None:
                if current1.val <= current2.val:
                    head.next = current1
                    current1 = current1.next
                else:
                    head.next = current2
                    current2 = current2.next
                
                head = head.next

            if current1 == None:
                head.next = current2
            else:
                head.next = current1

            return newHead