# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def maxzz(root, l, d):
            # print(" "*d, "L" if l else "R", d)
            if not root.left and not root.right: return d
            l1 = maxzz(root.left,True,1 if l else (d+1)) if root.left else d
            l2 = maxzz(root.right,False,(d+1) if l else 1) if root.right else d
            return max(l1,l2)

        l1 = maxzz(root.left,True,1) if root.left else 0
        l2 = maxzz(root.right,False,1) if root.right else 0
        return max(l1,l2)
