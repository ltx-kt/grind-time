# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        st = [[root, subRoot]]
        while st:
            t1, t2 = st.pop()
            if not t2:
                return True
            if not t1:
                continue
            if self.isSameTree(t1, t2):
                return True
            st.append([t1.left, t2])
            st.append([t1.right, t2])
        return False
        
    def isSameTree(self, p, q):
        st = [[p, q]]

        while st:
            t1, t2 = st.pop()
            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False
            st.append([t1.left, t2.left])
            st.append([t1.right, t2.right])
        return True
        