from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        def matrix_dfs(grid, curpos, curmax, curmin, depth=0):
            rowz = len(grid)
            colz = len(grid[0])
            r    = curpos[0]
            c    = curpos[1]
            #curmax = max(curmax*grid[r][c], curmin*grid[r][c])
            #curmin = min(curmax*grid[r][c], curmin*grid[r][c])
            curmax *= grid[r][c]
            print(" " * depth, r, c, "(", grid[r][c], ")", curmax, curmin)
            if r == rowz-1 and c == colz-1:
                return curmax, curmin
            max1 = max2 = -2**32
            min1 = min2 = 2**32
            if r < rowz-1:
                max1, min1 = matrix_dfs(grid, (r+1,c), curmax, curmin, depth+1)
            if c < colz-1:
                max2, min2 = matrix_dfs(grid, (r,c+1), curmax, curmin, depth+1)
            return max(max1, max2), min(min1, min2)

        maxm, minm = matrix_dfs(grid, (0,0), 1, 1)
        return maxm % (10**9 + 7) if maxm >= 0 else -1
            
S = Solution()
print(S.maxProductPath([[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]))
