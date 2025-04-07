# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root, depth, next_depth):
            # print(" "*depth, root.val, depth,next_depth)
            ans, chr, chl = (), (), ()
            if depth == next_depth:
                ans = (root.val,)
                next_depth += 1
            if root.right:
                chr = traverse(root.right, depth+1, next_depth)
            if root.left:
                chl = traverse(root.left, depth+1, next_depth + len(chr))
            return (*ans,*chr,*chl)

        if not root: return []
        tree = traverse(root,0,0)
        return list(tree)
