# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathsum(self, root, currsum):
        currsum *= 10
        currsum += root.val
        if not root.left and not root.right: return currsum
        final = 0
        if root.left: final += self.pathsum(root.left, currsum)
        if root.right: final += self.pathsum(root.right, currsum)
        return final

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.pathsum(root, 0)
