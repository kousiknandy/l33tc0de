# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pre_order(self, root):
        if root == None: return None, None
        lr, lt = self.pre_order(root.left)
        rr, rt = self.pre_order(root.right)
        root.left = None
        if lr:
            root.right = lr
            lt.right = rr
        else:
            root.right = rr
        return root, rt if rt else lt if lt else root

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre_order(root)
