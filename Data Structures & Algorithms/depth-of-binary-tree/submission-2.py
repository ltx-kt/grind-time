# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        st = [root]
        mp = {None: 0}
        if not root:
            return 0
        while st:
            node = st[-1]

            if node.left and node.left not in mp:
                st.append(node.left)
            elif node.right and node.right not in mp:
                st.append(node.right)
            else:
                node = st.pop()
                mp[node] = 1 + max(mp[node.left], mp[node.right])
        return mp[root]





