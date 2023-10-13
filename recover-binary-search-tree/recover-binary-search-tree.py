# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def in_order(self, root, left):
        # print(f"-{root.val}", end=" ")
        if not root.left and not root.right: 
            yield root
            return
        if left:
            if root.left: yield from self.in_order(root.left, left)
        else:
            if root.right: yield from self.in_order(root.right, left)
        yield root
        if left:
            if root.right: yield from self.in_order(root.right, left)
        else:
            if root.left: yield from self.in_order(root.left, left)


    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        for node in self.in_order(root, True):
            if not prev:
                prev = node
                continue
            if prev.val > node.val: break
            prev = node
        last = None
        for node in self.in_order(root, False):
            if not last:
                last = node
                continue
            if last.val < node.val: break
            last = node
        prev.val, last.val = last.val, prev.val
