class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        sol = [0] * len(mat) * len(mat[0])
        i, j = 0, 1
        r, c = 0, 0
        for i in range(len(sol)):
            try:
                if r < 0 or c < 0: raise IndexError
                sol[i] = mat[r][c]
                # print(i,r,c)
                r -= j
                c += j
            except IndexError:
                if j > 0: r += 1
                if j < 0: c += 1
                j *= -1
                try:
                    if r < 0 or c < 0: raise IndexError
                    sol[i] = mat[r][c]
                    # print(i,r,c)
                    r -= j
                    c += j
                except IndexError:
                    r -= j
                    c += j
                    if r < 0 or c < 0: raise IndexError
                    sol[i] = mat[r][c]
                    # print(i,r,c)
                    r -= j
                    c += j
        return sol        
