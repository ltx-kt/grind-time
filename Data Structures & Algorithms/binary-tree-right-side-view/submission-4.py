# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        st = [[root, 0]]

        while st:
            node, d = st.pop()

            if not node: 
                continue
            if len(res) == d:
                res.append(node.val)
            st.append([node.left, 1 + d])
            st.append([node.right, 1 + d])
        return res
