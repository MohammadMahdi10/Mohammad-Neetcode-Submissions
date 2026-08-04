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

            res = (left - right) + 1
            print(left, right, res)
            return res
                
        val = dfs(root)
        print(val)
        if val < 0 or val > 2:
            return False
        return True
