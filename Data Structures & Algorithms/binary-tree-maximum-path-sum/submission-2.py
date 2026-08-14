# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        st = [root]
        hm = {None: float('-inf')}
        res = float('-inf')

        while st:
            node = st[-1]
            if node.left and node.left not in hm:
                st.append(node.left)
            elif node.right and node.right not in hm:
                st.append(node.right)
            else:
                node = st.pop()
                lv = hm[node.left]
                rv = hm[node.right]
                path = max(node.val + max(lv, rv, lv + rv), node.val)
                hm[node] = max(node.val + max(lv, rv), node.val)
                res = max(res, path)
        return res