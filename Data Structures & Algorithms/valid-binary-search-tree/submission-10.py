# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        st = [[root, float('inf'), float('-inf')]]

        while st:
            node, upper, lower = st.pop()

            if not node:
                continue
            
            if not lower < node.val < upper:
                return False
            
            st.append([node.left, node.val, lower])
            st.append([node.right, upper, node.val])
        return True
