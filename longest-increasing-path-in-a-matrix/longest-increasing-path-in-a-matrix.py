class Solution:
    def nextmove(self, matrix, i, j):
        m, n = len(matrix), len(matrix[0])
        if 1 <= i <= m-1 and matrix[i-1][j] > matrix[i][j]: yield i-1,j
        if 0 <= i < m-1 and matrix[i+1][j] > matrix[i][j]: yield i+1,j
        if 1 <= j <= n-1 and matrix[i][j-1] > matrix[i][j]: yield i,j-1
        if 0 <= j < n-1 and matrix[i][j+1] > matrix[i][j]: yield i,j+1

    def dfs_traverse(self, matrix, i, j, depth, mem):
        if mem[i][j] is not None: return depth + mem[i][j]
        paths = [self.dfs_traverse(matrix, p, q, 0, mem) + 1 for p,q in self.nextmove(matrix,i,j)]
        # print("  ", i,j,paths)
        mem[i][j] = max(paths) if paths else 1
        return depth + mem[i][j]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        mem =[[None] * n for _ in range(m)]
        res = []
        for i in range(m):
            for j in range(n):
                pathsz = self.dfs_traverse(matrix, i, j, 0, mem)
                res.append(pathsz)
                # print(i,j,pathsz)
        # print(mem)
        return max(res)
