from typing import List
class Solution:
    def next_pos(self, grid, cur, path):
        r, c = cur
        rows, cols = len(grid), len(grid[0])
        moves = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
        for mr,mc in moves:
            if 0 <= mr < rows and 0 <= mc < cols:
                if grid[mr][mc] in [0,2]:
                    if (mr, mc) not in path:
                        yield mr, mc, path[:] + [(mr,mc)]

    
    def find_1(self, grid: List[List[int]]) -> (int, int):
        zeros = 0
        oner, onec = 0, 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    oner, onec = r, c
                if grid[r][c] != -1:
                    zeros += 1
        return oner, onec, zeros

    def trace_path(self, grid, cur, path, pathlen):
        count = 0
        for nr, nc, npath in self.next_pos(grid, cur, path):
            if grid[nr][nc] == 2 and len(path) == pathlen:
                count += 1
                #print(path, len(path), pathlen)
                continue
            count += self.trace_path(grid, (nr,nc), npath, pathlen)
        return count
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        startr, startc, pathlen = self.find_1(grid)
        paths = self.trace_path(grid, (startr, startc), [(startr, startc)], pathlen-1)
        return paths

S = Solution()
print(S.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
