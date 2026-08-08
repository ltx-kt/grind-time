# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        st = [[root, 1]]
        res = 0
        while st:
            node, height = st.pop()

            if not node:
                continue
            
            res = max(res, height)
            st.append([node.left, height + 1])
            st.append([node.right, height + 1])

        return res