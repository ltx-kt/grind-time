# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        st = [[p, q]]

        while st:
            r, l = st.pop()
            if not r and not l:
                continue
            
            if not r or not l:
                return False
            if r.val != l.val:
                return False
            
            st.append([r.left, l.left])
            st.append([r.right, l.right])
        return True
