from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        minutes = [[0] * n for _ in range(m)]
        start = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: minutes[i][j] = -1
                if grid[i][j] == 2: start.append((i,j))
        for i,j in start:
            visited = set()
            bfsq = deque()
            bfsq.append((i,j,0))
            while len(bfsq) > 0:
                i,j,d = bfsq.popleft()
                if (i,j) in visited: continue
                visited.add((i,j))
                if minutes[i][j] > 0: minutes[i][j] = min(d, minutes[i][j])
                else: minutes[i][j] = d
                if i > 0 and grid[i-1][j] == 1: bfsq.append((i-1,j,d+1))
                if i < m-1 and grid[i+1][j] == 1: bfsq.append((i+1,j,d+1))
                if j > 0 and grid[i][j-1] == 1: bfsq.append((i,j-1,d+1))
                if j < n-1 and grid[i][j+1] == 1: bfsq.append((i,j+1,d+1))
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, minutes[i][j])
                if minutes[i][j] == -1:
                    return -1
        return ans 
