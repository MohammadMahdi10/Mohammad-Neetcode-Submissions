# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def BFS(root1, root2):
            queue = deque()
            queue2 = deque()

            if root1:
                queue.append(root1)
            if root2:
                queue2.append(root2)
            
            while len(queue) > 0:
                if len(queue2) < 0:
                    return False
                for i in range(len(queue)):
                    curr = queue.popleft()
                    curr2 = queue2.popleft()
                    if curr == None or curr2 == None or curr.val != curr2.val:
                        if curr == None and curr2 == None:
                            continue
                        else:
                            return False

                    queue.append(curr.left)
                    queue.append(curr.right)
                    
                    queue2.append(curr2.left)
                    queue2.append(curr2.right)

            if len(queue) > 0 or len(queue2) > 0:
                return False
            return True
        val = BFS(p, q)
        return val