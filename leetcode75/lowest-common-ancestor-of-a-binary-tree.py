# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def search_pq(self, root, p, q):
        if root in [p,q]: return root
        l = self.search_pq(root.left, p, q) if root.left else None
        r = self.search_pq(root.right, p, q) if root.right else None
        if l and r: return root
        return l or r

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        n = self.search_pq(root,p,q)
        return n
