class Solution:

    def next_turn(self):
        yield from itertools.cycle([(0,1),(1,0),(0,-1),(-1,0)]) # E->S->W->N

    def gen_spiral(self, n):
        gd = self.next_turn()
        yield from itertools.repeat(next(gd), n-1)
        for i in range(n-1):
            yield from itertools.repeat(next(gd), n-i-1)
            yield from itertools.repeat(next(gd), n-i-1)

    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for j in range(n)]
        r, c, k = 0, 0, 1
        res[r][c] = k
        for i, j in self.gen_spiral(n):
            r, c, k = r+i, c+j, k+1
            res[r][c] = k
        return res
