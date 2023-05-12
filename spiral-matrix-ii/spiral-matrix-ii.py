class Solution:
    mv = {'E': (0,1), 'W': (0,-1), 'N': (-1,0), 'S': (1,0)}

    def nextdir(self):
        yield from itertools.cycle("ESWN")

    def go_spiral(self, n):
        gd = self.nextdir()
        d = next(gd)
        for _ in range(n-1): yield d
        for i in range(n-1):
            d = next(gd)
            for _ in range(n-i-1): yield d
            d = next(gd)
            for _ in range(n-i-1): yield d

    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for j in range(n)]
        k = 1
        r, c = 0, 0
        # print(r,c,k)
        res[r][c] = k
        for d in self.go_spiral(n):
            i, j = self.mv[d]
            r += i
            c += j
            k += 1
            # print(d, r,c,k)
            res[r][c] = k
        return res
