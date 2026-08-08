# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[1]
    def dfs(self, root):
        if not root:
            return 0, 0
        
        lh, ld = self.dfs(root.left)
        rh, rd = self.dfs(root.right)
        height = 1 + max(lh, rh)
        diameter = max(ld, rd, lh + rh)
        return height, diameter