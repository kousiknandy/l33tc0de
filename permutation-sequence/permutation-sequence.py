class Solution:
    fact = [362880, 40320, 5040, 720, 120, 24, 6, 2, 1]


    def rotations(self, k):
        s = []
        for f in self.fact:
            s.append(k//f)
            k %= f
        return s
    
    def getPermutation(self, n: int, k: int) -> str:
        s = [str(x) for x in range(1,n+1)]
        f = self.rotations(k-1)[-n+1:]
        for i in range(n-1):
            self.bubble(s,i,i+f[i])
        return "".join(s)

    def bubble(self, s, i, j):
        k = s[i]
        s[i] = s[j]
        for l in range(j,i+1,-1):
            s[l] = s[l-1]
        if j>i: s[i+1] = k
            
        
