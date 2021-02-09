from typing import List

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int, d: int = 1) -> int:
        output = 0
        i = 0
        j = 0
        n = dict()
        if len(A) == 0:
            return 0
        n[A[i]] = 1
        print("*"*d, A)
        while True:
            print(" "*d, A[i:j+1])
            if len(A[i:j+1]) == 0:
                return output
            if len(n) > K or j >= len(A):
                c = n.get(A[i], 0)
                if c == 1:
                    n.pop(A[i])
                else:
                    n[A[i]] = c - 1
                i += 1
                output += self.subarraysWithKDistinct(A[i:j+1], K, d+1) 
                if j >= len(A):
                    break
                i = j = j + 1
                n = dict()
                if i < len(A):
                    n[A[i]] = 1
                continue
            if len(n) == K:
                output += 1
                print(" "*d, "^ ", output, n)
            while True:
                j += 1
                if j < len(A):
                    c = n.get(A[j], 0)
                    n[A[j]] = c + 1
                    if j < len(A) - 1:
                        if A[j] == A[j+1]:
                            continue
                break
        return output

S = Solution()
print(S.subarraysWithKDistinct([1,2], 2)) #1
print(S.subarraysWithKDistinct([1,2,1,2,3], 2)) #7
print(S.subarraysWithKDistinct([1,2,1,3,4],3)) #3
print(S.subarraysWithKDistinct([1,2],1)) #2
print(S.subarraysWithKDistinct([1,2,1],1)) #3
print(S.subarraysWithKDistinct([1],1)) #1
print(S.subarraysWithKDistinct([1,1,1,2,1,2,2,1], 1)) #12
print(S.subarraysWithKDistinct([1,2,2],1)) #4
print(S.subarraysWithKDistinct([1,1,1],1)) #6

