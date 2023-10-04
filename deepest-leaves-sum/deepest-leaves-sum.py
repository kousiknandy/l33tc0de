# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depthsum(self, root, depth, deepsum):
        if root.left == None and root.right == None:
            cs = root.val + (deepsum[0] if deepsum[1] == depth else 0)
            return (cs, depth)
        csl = self.depthsum(root.left, depth+1, deepsum) if root.left else (0,0)
        csr = self.depthsum(root.right, depth+1, deepsum) if root.right else (0,0)
        if csr[1] == csl[1]:
            if deepsum[1] > csr[1]: return deepsum
            cs = csl[0] + csr[0]
            if deepsum[1] == csl[1]:
                cs += deepsum[0]
            return (cs, csl[1])
        if csl[1] > csr[1]:
            if deepsum[1] > csl[1]: return deepsum
            return (csl[0] + (deepsum[0] if csl[1] == deepsum[1] else 0), csl[1])
        if deepsum[1] > csr[1]: return deepsum
        return (csr[0] + (deepsum[0] if csr[1] == deepsum[1] else 0), csr[1])
        

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        s, d = self.depthsum(root, 0, (0,0))
        return s
