# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _depth(node, depth):
            if node is None: return depth
            d1 = _depth(node.left, depth+1) 
            d2 = _depth(node.right, depth+1)
            return max(d1,d2)
        return _depth(root,0)
