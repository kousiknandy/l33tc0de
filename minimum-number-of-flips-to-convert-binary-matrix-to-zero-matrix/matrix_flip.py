from graphutils import Graph

class BinMatrix:
    def __init__(self, mat):
        self.mat = mat
        self.sz  = len(mat) * len(mat[0])

    def seq(self):
        s = ""
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                s = s + str(self.mat[i][j])
        print(s)
        return int(s,2)

    def is_zero(self):
        return self.seq() == 0

    def flip(self, row, col):
        new_mat = self.mat
        if new_mat[row][col] == 0:
            new_mat[row][col] = 1
        else:
            new_mat[row][col] = 0

        try:
            if new_mat[row+1][col] == 0:
                new_mat[row+1][col] = 1
            else:
                new_mat[row+1][col] = 0
        except:
            pass
        
        try:
            if new_mat[row-1][col] == 0:
                new_mat[row-1][col] = 1
            else:
                new_mat[row-1][col] = 0
        except:
            pass
        try:
            if new_mat[row][col+1] == 0:
                new_mat[row][col+1] = 1
            else:
                new_mat[row][col+1] = 0
        except:
            pass
        
        try:
            if new_mat[row][col-1] == 0:
                new_mat[row][col-1] = 1
            else:
                new_mat[row][col-1] = 0
        except:
            pass
        return new_mat

if __name__ == "__main__":
    b = BinMatrix([[1,1,1],[1,0,1],[0,0,0]])
    print(b.sz, b.seq())
    c = b.flip(1,0)
    c = BinMatrix(c)
    print(c, c.sz, c.seq())
    b = BinMatrix([[0,0,0],[1,0,1],[0,0,0]])
    print(b.sz, b.seq())
    b = BinMatrix([[0,0,0],[0,0,0],[0,0,0]])
    print(b.sz, b.seq())
    b = BinMatrix([[1,1],[1,1]])
    print(b.sz, b.seq())
    b = BinMatrix([[0]])
    print(b.sz, b.seq())
    b = BinMatrix([[1,1,1],[1,1,1],[1,1,1]])
    print(b.sz, b.seq())
    c = b.flip(1,1)
    c = BinMatrix(c)
    print(c, c.sz, c.seq())
