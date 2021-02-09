# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def checkBST(self, node, vmin = None, vmax = None)
        if vmin and not node.val > vmin:
            return False
        if vmax and not node.val < vmax:
            return False
        
        if node.left and not self.checkBST(node.left,
                                           vmin,
                                           node.val)
            return False
        if node.right and not self.checkBST(node.right,
                                            node.val,
                                            vmax)
            return False
        return True
        
    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkBST(root)

