from functools import partial
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def nextmove(maze,m,n,i,j):
            if j > 0 and maze[i][j-1] == ".": yield i,j-1
            if j < n-1 and maze[i][j+1] == ".": yield i,j+1
            if i > 0 and maze[i-1][j] == ".": yield i-1,j
            if i < m-1 and maze[i+1][j] == ".": yield i+1,j
        
        def isexit(m,n,er,ec,i,j):
            if er == i and ec == j: return False
            if i == 0 or i == m-1 or j == 0 or j == n-1: return True
            return False

        m = len(maze)
        n = len(maze[0])
        er, ec = entrance[0], entrance[1]

        nextmove = partial(nextmove,maze=maze,m=m,n=n)
        isexit = partial(isexit,m=m,n=n,er=er,ec=ec)
        visited = set()
        bfsq = deque()
        bfsq.append((er,ec,0))
        while len(bfsq) > 0:
            i, j, s = bfsq.popleft()
            if (i,j) in visited: continue
            else: visited.add((i,j))
            # print(i,j,s,isexit(i=i,j=j))
            if isexit(i=i,j=j): return s
            for p,q in nextmove(i=i,j=j):
                bfsq.append((p,q,s+1))
        return -1
