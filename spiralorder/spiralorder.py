class SpiralMatrix:
    def __init__(self, A):
        self.matrix = A
        self.rowsize = len(A)
        self.colsize = len(A[0])
        self.pos = (0, 0)
        self.dir = [(0, 1, 1, 0, 0, 0),
                    (1, 0, 0, 0, 0, -1),
                    (0, -1, 0, -1, 0, 0),
                    (-1, 0, 0, 0, 1, 0)]
        self.currdir = 0

    def __iter__(self):
        self.rowmin = 0
        self.rowmax = self.rowsize - 1
        self.colmin = 0
        self.colmax = self.colsize - 1
        self.pos = (0, 0)
        return self
    
    def __next__(self):
        p = self.pos
        print(p)
        print(" ", self.rowmin, self.rowmax, self.colmin, self.colmax)
        n = (p[0] + self.dir[self.currdir][0], p[1] + self.dir[self.currdir][1])
        print(" ", self.currdir, n)
        if (n[0] < self.rowmin) or (n[1] < self.colmin) or \
           (n[0] > self.rowmax) or (n[1] > self.colmax):
            print("  ", self.rowmin, self.rowmax, self.colmin, self.colmax)
            self.rowmin += self.dir[self.currdir][2]
            self.rowmax += self.dir[self.currdir][3]
            self.colmin += self.dir[self.currdir][4]
            self.colmax += self.dir[self.currdir][5]
            if self.rowmin > self.rowmax or self.colmin > self.colmax:
                raise StopIteration
            self.currdir = (self.currdir + 1) % len(self.dir)
            n = (p[0] + self.dir[self.currdir][0], p[1] + self.dir[self.currdir][1])            
            print("   ", self.currdir, n)
        self.pos = n
        return p
        

class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        SPA = SpiralMatrix(A)
        for p in SPA:
            #print("    ", A[p[0]][p[1]], p)
            yield A[p[0]][p[1]]

S = Solution()
s = S.spiralOrder([[1,2,3],[8,9,4],[7,6,5]])
s = S.spiralOrder([[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]])
s = S.spiralOrder([ [1, 2],  [3, 4],  [5, 6]])
s = S.spiralOrder([[1,2]])
s = S.spiralOrder([[1]])
for i in s:
    print(i)
