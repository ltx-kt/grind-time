# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0

        st = [(root, 1)]

        while st:
            node, h = st.pop()
            if not node:
                 continue
            res = max(res, h)

            st.append((node.left, h + 1))
            st.append((node.right, h + 1))
        
        return res
