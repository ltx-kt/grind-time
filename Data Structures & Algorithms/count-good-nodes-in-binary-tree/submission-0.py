# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        st = [[root, root.val]]
        res = 0
        while st:
            node, maxVal = st.pop()
            if not node:
                continue
            if node.val >= maxVal:
                print(node.val)
                res +=1
            st.append([node.left, max(node.val, maxVal)])
            st.append([node.right, max(node.val, maxVal)])
        return res

            
