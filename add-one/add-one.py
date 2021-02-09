class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        if len(A) == 0:
            return [1]
        while A[0] == 0:
            A.pop(0)
            if len(A) == 0:
                return [1]
        c = 0
        d = A[-1]
        d += 1
        A[-1] = d % 10
        c = d // 10
        if c == 0:
            return A
        if len(A) >= 2:
            for j in range(len(A) - 2, -1, -1):
                d = A[j]
                d = d + c
                A[j] = d % 10
                c = d // 10
                if c == 0:
                    break
        if c > 0:
            A.insert(0, c)
        return A

S = Solution()
print(S.plusOne([1, 2, 3]))
print(S.plusOne([9]))
print(S.plusOne([9, 9]))
print(S.plusOne([9, 9, 9]))
print(S.plusOne([1, 2, 9]))
print(S.plusOne([0]))
print(S.plusOne([0, 0 , 9, 1, 2, 3]))


