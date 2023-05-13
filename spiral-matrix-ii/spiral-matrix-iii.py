class Solution:

    def next_turn(self):
        yield from itertools.cycle([(0,1),(1,0),(0,-1),(-1,0)])

    def gen_spiral(self):
        gd = self.next_turn()
        i = 1
        while True:
            yield from itertools.repeat(next(gd), i)
            yield from itertools.repeat(next(gd), i)
            i += 1

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        r, c, k = rStart, cStart, 1
        res.append([r,c])                
        for i, j in self.gen_spiral():
            r += i
            c += j
            if 0 <= r < rows and 0 <= c < cols:
                k += 1
                res.append([r,c])                
            if k >= rows * cols: 
                break
        return res
