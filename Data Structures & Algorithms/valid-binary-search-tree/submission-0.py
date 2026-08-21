# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def DFS(curr, left, right):
            if not curr:
                return True

            if not (curr.val < right and curr.val > left):
                return False
            
            return DFS(curr.left, left, curr.val) and DFS(curr.right, curr.val, right)
            
        
        return DFS(root, float("-infinity"), float("infinity"))