class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rm = [max(grid[r]) for r in range(m)]
        cm = [max([grid[i][j] for i in range(m)]) for j in range(n)]
        # newgrid = [[0] * n for _ in range(m)]
        height = 0
        for r in range(m):
            for c in range(n):
                # newgrid[r][c] = min(rm[r], cm[c])
                height += min(rm[r], cm[c]) - grid[r][c]
        # print(rm, cm, newgrid)
        return height
