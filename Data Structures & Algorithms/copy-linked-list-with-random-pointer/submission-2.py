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
        maps = {}

        newHead = Node(0)
        curr = newHead

        prevCur = head
        while prevCur:
            newNode = Node(prevCur.val)

            maps[prevCur] = newNode

            curr.next = newNode
            curr = curr.next
            prevCur = prevCur.next
        
        curr = newHead.next
        prevCur = head

        while prevCur:
            if prevCur.random == None:
                curr.random = None
            else:
                curr.random = maps[prevCur.random]

            prevCur = prevCur.next
            curr = curr.next
        return newHead.next



        