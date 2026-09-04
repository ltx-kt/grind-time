# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        st = [root]
        hm = {None: 0}
        d = 0
        while st:
            node = st[-1]

            if not node:
                continue
            if node.left and node.left not in hm:
                st.append(node.left)
            elif node.right and node.right not in hm:
                st.append(node.right)
            else:
                node = st.pop()
                lh = hm[node.left]
                rh = hm[node.right]

                d = max(d, lh + rh)
                hm[node] = 1 + max(lh, rh)
        return d