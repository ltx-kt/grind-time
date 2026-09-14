# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, m):
            if not node:
                return 0
            if node.val < m:
                res = 0
            else:
                res = 1
            mv = max(m, node.val)
            res += (dfs(node.left, mv) + dfs(node.right, mv))
            return res
        return dfs(root, root.val)