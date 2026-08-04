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

            res = left - right
            print(left, right, res)
            return 1 + res
                
        val = dfs(root)
        print(val)
        if val <= -1 or val >= 3:
            return False
        return True
