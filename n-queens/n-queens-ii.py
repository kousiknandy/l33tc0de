class Solution:
    def next_column(self, row, cols, ldiag, rdiag):
        for c in range(self.n):
            if c not in cols and (row-c) not in ldiag and (self.n-1-row-c) not in rdiag: 
                yield c

    def add_queen(self, row, cols, ldiag, rdiag):
        if row == self.n:
            self.sols += 1
            return
        for c in self.next_column(row, cols, ldiag, rdiag):
            cdash = cols[:] + [c]
            ldiagdash = ldiag[:] + [row-c]
            rdiagdash = rdiag[:] + [self.n-1-row-c]
            self.add_queen(row+1, cdash, ldiagdash, rdiagdash)

    
    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.sols = 0
        for c in range(n):
            self.add_queen(1, [c], [-c], [self.n-1-c])
        return self.sols
