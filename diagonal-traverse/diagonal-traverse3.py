class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        result = []
        b = 1
        for i in range(m+n-1):
            if b > 0: 
                r = min(i,m-1)
                c = i-r
            else: 
                c = min(i,n-1)
                r = i -c
            for j in range(min(i,m,n)+1):
                if 0<=r<m and 0<=c<n:
                    result.append(mat[r][c])
                # print(i,r,c, result)
                r-=b
                c+=b
            b = -b
        return result
