# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:

    def bfs(self, root: TreeNode):
        depth = 0
        bfs_q = deque([(root, depth)])
        while len(bfs_q) > 0:
            node, depth = bfs_q.popleft()
            if node.left:
                bfs_q.append((node.left, depth+1))
            if node.right:
                bfs_q.append((node.right, depth+1))
            yield node.val, depth
    
    def maxLevelSum(self, root: TreeNode) -> int:
        levelsum = []
        for value, level in self.bfs(root):
            if len(levelsum) < level+1:
                levelsum.append(0)
            levelsum[level] += value
        print(levelsum)
        maxsum = max(levelsum)
        return levelsum.index(maxsum)


a, b, c, d, e, f, g = [TreeNode(ord('a')+_) for _ in range(7)]
for x in [a, b, c, d, e, f, g]: print(x.val, end=" ")
a.left = b
a.right = g
b.left = c
b.right = d
d.left = e
g.right = f
S = Solution()
print(S.maxLevelSum(a))
