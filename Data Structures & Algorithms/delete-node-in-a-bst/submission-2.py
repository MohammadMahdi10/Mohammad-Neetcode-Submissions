# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNode(self, root):
        cur = root
        while cur and cur.left:
            cur = cur.left
        return cur
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        # search for node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # 0 or 1 children
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                # 2 children
                minVal = self.minNode(root.right)
                root.val = minVal.val
                root.right = self.deleteNode(root.right, minVal.val)
        return root









