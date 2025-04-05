# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        stack = []
        if not root: return 0
        stack.append((root,False,False))
        stksum = lambda stk: sum(s[0].val for s in stk)
        count = 0
        while len(stack) > 0:
            # print(count, [(s[0].val,s[1],s[2]) for s in stack])
            if not stack[-1][1] and not stack[-1][2]:
                tot = 0
                for i in range(len(stack)-1,-1,-1):
                    tot += stack[i][0].val
                    if tot == targetSum: count += 1 
            if stack[-1][0].left and not stack[-1][1]:
                stack[-1] = (stack[-1][0], True, stack[-1][2])
                stack.append((stack[-1][0].left,False,False))
                continue
            if stack[-1][0].right and not stack[-1][2]:
                stack[-1] = (stack[-1][0], stack[-1][1], True)
                stack.append((stack[-1][0].right,False,False))
                continue
            stack.pop()
        return count
