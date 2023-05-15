class Solution:
    def next_column(self, cols):
        row = len(cols)
        ldiag = [x[0]-x[1] for x in zip(range(row), cols)]
        rdiag = [self.n-1-x[0]-x[1] for x in zip(range(row), cols)]
        for c in range(self.n):
            if c not in cols and (row-c) not in ldiag and (self.n-1-row-c) not in rdiag: 
                yield c

    def add_queen(self, cols):
        if len(cols) == self.n:
            self.add_solution(cols)
            return
        for c in self.next_column(cols):
            cdash = cols[:] + [c]
            self.add_queen(cdash)

    def print_row(self, c):
        s = "."*(c) + "Q" + "."*(self.n-c-1)
        return s

    def add_solution(self, cols):
        s = []
        for c in cols:
            s.append(self.print_row(c))
        self.sols.append(s) 

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.sols = []
        for c in range(n):
            self.add_queen([c])
        return self.sols
