# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(root):
            if not root.left and not root.right: yield root.val
            if root.left: yield from leaves(root.left)
            if root.right: yield from leaves(root.right)

        leaves1 = leaves(root1)
        leaves2 = leaves(root2)
        while True:
            try:
                l1 = next(leaves1)
            except StopIteration:
                l1 = None
            try:
                l2 = next(leaves2)
            except StopIteration:
                l2 = None
            # print(l1, l2)
            if l1 != l2: return False
            if l1 is None and l2 is None: break
        return True
