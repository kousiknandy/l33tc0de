# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countgood(root, pathmax):
            count = 0
            if root.val >= pathmax: count += 1
            pathmax = max(pathmax, root.val)
            cl = countgood(root.left, pathmax) if root.left else 0
            cr = countgood(root.right, pathmax) if root.right else 0
            return count + cl + cr

        return countgood(root, root.val)
