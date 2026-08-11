# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # res = []
        # st = [[root, 0]]
        # while st:
        #     node, level = st.pop()
        #     if not node:
        #         continue
        #     if level == len(res):
        #         res.append([])
        #     res[level].append(node.val)
        #     st.append([node.right, level + 1])
        #     st.append([node.left, level + 1])
        # return res

        res = []
        def dfs(root, lvl):
            if not root:
                return None
            if lvl == len(res):
                res.append([])
            res[lvl].append(root.val)
            dfs(root.left, lvl + 1)
            dfs(root.right, lvl + 1)
        dfs(root, 0)
        return res


