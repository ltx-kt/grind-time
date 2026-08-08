# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]
    
    def dfs(self, root):
        if not root:
            return True, 0
        lb, lh = self.dfs(root.left)
        rb, rh = self.dfs(root.right)
        return (lb and rb and abs(lh - rh) <= 1, 1 + max(lh, rh))