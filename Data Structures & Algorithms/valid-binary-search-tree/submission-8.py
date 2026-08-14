# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        st = [[root, float('-inf'), float('inf')]]

        while st:
            node, left, right = st.pop()

            if not node:
                continue

            if not left < node.val < right:
                return False
            st.append([node.left, left, node.val])
            st.append([node.right, node.val, right])
        return True