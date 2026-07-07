"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        randomHolds = {}
        
        newHead = None
        current = head
        prev = None

        while current != None:
            newNode = Node(current.val)
            
            if prev != None:
                prev.next = newNode
            else:
                newHead = newNode
            
            randomHolds[current] = newNode
            prev = newNode
            current = current.next

        newCurrent = newHead
        current = head


        while current != None:
            if current.random == None:
                newCurrent.random = None
            else:
                newCurrent.random = randomHolds[current.random]

            current = current.next
            newCurrent = newCurrent.next
        
        return newHead
                



        