# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur):
            if not cur:
                return 0
            
            left = dfs(cur.left)
            right = dfs(cur.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return 1 + max(left, right)
                
        val = dfs(root)
        if val == -1:
            return False
        return True
