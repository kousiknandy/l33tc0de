# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchpath(self, root, p, q, path):
        if root == p: 
            self.p = path[:]
            self.p.append(p)
        if root == q:
            self.q = path[:]
            self.q.append(q)
        if self.p and self.q: return
        if root.left:
            newpath = path[:]
            newpath.append(root)
            self.searchpath(root.left, p, q, newpath)
            if self.p and self.q: return
        if root.right:
            newpath = path[:]
            newpath.append(root)
            self.searchpath(root.right, p, q, newpath)
            if self.p and self.q: return


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = []
        self.q = []
        self.searchpath(root, p, q, [])
        ans = root
        for pp,pq in zip(self.p, self.q):
            if pp.val != pq.val: break
            ans = pp
        return ans 
