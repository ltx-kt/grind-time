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
            node, lb, ub = st.pop()

            if not node:
                continue
            
            if not lb < node.val < ub:
                return False
            
            st.append([node.left, lb, node.val])
            st.append([node.right, node.val, ub])
        return True