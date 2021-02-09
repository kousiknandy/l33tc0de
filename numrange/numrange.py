class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        i = 0
        j = 0
        sm = A[i]
        ranges = 0
        while True:
            #print(i, j, sm, ranges)
            if sm > C:
                sm -= A[i]
                i += 1
                if i > len(A) - 1:
                    break
                j = i
                sm = A[i]
                continue
            if sm < B:
                j += 1
                if j > len(A) - 1:
                    sm -= A[i]
                    i += 1
                    if i > len(A) - 1:
                        break
                    j = i
                    sm = A[j]
                    continue
                sm += A[j]
                continue
            ranges += 1
            #print(" ", A[i:j+1], "=", sm)
            if j < len(A) - 1:
                j += 1
                sm += A[j]
                continue
            sm -= A[i]
            i += 1
            if i > len(A) - 1:
                break
            j = i
            sm = A[j]
            
        return ranges

S = Solution()
print(S.numRange([10, 5, 1, 0, 2], 6, 8)) #3
print(S.numRange([1, 5, 1, 3, 2], 6, 6)) #3
print(S.numRange([1, 1, 1, 1, 1], 3, 4)) #5
print(S.numRange([1], 0, 0)) #0
print(S.numRange([ 76, 22, 81, 77, 95, 23, 27, 35, 24, 38, 15, 90, 19, 46, 53, 6, 77, 96, 100, 85, 43, 16, 73, 18, 7, 66 ], 98, 290)) #84
print(S.numRange([ 94, 21, 6, 30, 70, 57, 78, 27, 18, 41, 36, 15, 95, 24, 2, 55, 25, 48 ], 46, 369)) #108
