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
            randomVal = current.random.val if current.random != None else None
            randomHolds[current.val] = randomVal
            newNode = Node(current.val)
            
            if prev != None:
                prev.next = newNode
            else:
                newHead = newNode
            
            prev = newNode
            current = current.next

        newCurrent = newHead

        while newCurrent != None:
            nxt = newHead
            num = randomHolds[newCurrent.val]

            if num == None:
                newCurrent.random = None
            else:
                while nxt != None and nxt.val != num:
                    nxt = nxt.next
                newCurrent.random = nxt
            
            newCurrent = newCurrent.next
        
        return newHead
                



        