class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def isqrt(n):
            x = n
            y = (x + 1) // 2
            while y < x:
                x = y
                y = (x + n // x) // 2
            return x
        
        def grow(r, c, sqs, matrix):
            if matrix[r][c] == "0":
                sqs[r][c] = 0
                return 0
            try:
                b = sqs[r+1][c+1]
            except:
                sqs[r][c] = 1 if matrix[r][c] == "1" else 0
                return 1
            if b == 0:
                sqs[r][c] = 1 if matrix[r][c] == "1" else 0
                return 1
            s = isqrt(b)+1
            rr, cc = 0, 0
            print(r,c,s)
            for i in range(s):
                if matrix[r][c+i] == "1": rr += 1
                else: break
            for i in range(s):
                if matrix[r+i][c] == "1": cc += 1
                else: break    
            s = min(rr,cc)
            sqs[r][c] = s*s
            return s*s

        m = len(matrix)
        n = len(matrix[0])
        sqs = [[0]*n for _ in range(m)]
        mx = 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mx = max(mx, grow(i,j,sqs,matrix))
        # print(sqs)
        return mx
