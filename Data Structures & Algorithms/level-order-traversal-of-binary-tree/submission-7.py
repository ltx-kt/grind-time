# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        st = [[root, 0]]
        res = []
        while st:
            node, d = st.pop()

            if not node:
                continue

            if d == len(res):
                res.append([])
            
            res[d].append(node.val)
            st.append([node.right, 1 + d])
            st.append([node.left, 1 + d])
        return res

            