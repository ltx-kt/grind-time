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
            t1, t2 = st.pop()
            if not t1 and not t2:
                continue
            if t1 and t2 and t1.val == t2.val:
                st.append([t1.left, t2.left])
                st.append([t1.right, t2.right])
            else:
                return False
        return True