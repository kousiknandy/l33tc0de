class Solution:

    mem = {0: 0, 1: 1, 2: 2}
    
    def ways2eat(self, n, days = 0):
        #print(" " * days, n)
        if n in self.mem:
            return self.mem[n]
        e1 = e2 = e3 = 1000000
        if n % 2 == 0:
            e2 = 1 + self.ways2eat(n//2, days+1)
        if n % 3 == 0:
            e3 = 1 + self.ways2eat(n//3, days+1)
        if n % 2 or n % 3:
            e1 = 1 + self.ways2eat(n-1, days+1)
        mindays = min((e1, e2, e3))
        #print(" " * days, n, "[", e1, e2, e3, "]", mindays)
        self.mem[n] = mindays
        return mindays
    
    def minDays(self, n: int) -> int:
        return self.ways2eat(n, 0)

S = Solution()
print(S.minDays(3))
print(S.minDays(6))
print(S.minDays(10))
print(S.minDays(820592))
# for X in range(20):
#     print(X, S.minDays(X))

