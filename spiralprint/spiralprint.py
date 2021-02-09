class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        solution = [[0 for _ in range(2*A-1)] for _ in range(2*A-1)]
        for k in range(A, 0, -1):
            for r in range(2*k-1):
                solution[A-k][A-k+r] = k
                solution[A+k-2][A-k+r] = k
            for r in range(2*k-1):
                solution[A-k+r][A-k] = k
                solution[A-k+r][A+k-2] = k
        return solution


S = Solution()
print(S.prettyPrint(5))

        
