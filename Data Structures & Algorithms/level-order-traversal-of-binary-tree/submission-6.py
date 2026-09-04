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
            node, depth = st.pop()

            if not node:
                continue
            if depth == len(res):
                res.append([])

            res[depth].append(node.val)

            st.append([node.right, depth + 1])
            st.append([node.left, depth + 1])
        return res
            
