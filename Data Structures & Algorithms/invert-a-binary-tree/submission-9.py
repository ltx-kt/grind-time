# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        st = []
        st.append(root)
        hm = set()
        diameter = 0
        while st:
            node = st[-1]
            if node.left and node.left not in hm:
                st.append(node.left)
            elif node.right and node.right not in hm:
                st.append(node.right)
            else:
                node = st.pop()
                node.left, node.right = node.right,node.left
                hm.add(node)
        return root