# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        p = root
        q = subRoot

        if not p and q:
            return False
        if not p and not q:
            return True
        if not q and p:
            return True

        if p.val == q.val:
            return (self.isSubtree(p.left, q.left) and self.isSubtree(p.right, q.right))
        else:
            return False
