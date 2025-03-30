import hashlib

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def djb(buf):
            h = 0x1505
            for b in buf:
                h = (h << 5) + h + b
            return  ((h >> 24) ^ h) & ((1 << 24) - 1)
        def md(buf):
            ba = []
            for b in buf: ba.extend(b.to_bytes(32))
            return hashlib.md5(bytearray(ba)).hexdigest()

        checker = {}
        hashfunction = md
        for row in grid:
            h = hashfunction(row)
            # print(row, h)
            if h in checker: checker[h] = (checker[h][0]+1, checker[h][1])
            else: checker[h] = (1, 0)
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            h = hashfunction(col)
            # print(col,h)
            if h in checker: checker[h] = (checker[h][0], checker[h][1]+1)
            else: checker[h] = (0, 1)
        print(checker)
        ans = sum(c[0]*c[1] for c in checker.values())
        return ans
