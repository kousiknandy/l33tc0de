from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        bfsq = deque()
        mxlvl = (root.val, 1)
        curlvl = 1
        bfsq.append((root, curlvl))
        lvlsum = 0
        while len(bfsq) > 0:
            node, lvl = bfsq.popleft()
            # print(node.val,lvl,lvlsum,mxlvl)
            if lvl == curlvl:
                lvlsum += node.val
            else:
                if lvlsum > mxlvl[0]:
                    mxlvl = (lvlsum, curlvl)
                lvlsum = node.val
            if node.left: bfsq.append((node.left, lvl+1))
            if node.right: bfsq.append((node.right, lvl+1))
            curlvl = lvl
        if lvlsum > mxlvl[0]:
            mxlvl = (lvlsum, curlvl)
        return mxlvl[1]
