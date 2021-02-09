class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        L       = lcm(A, B)
        tilllcm = L // A + L // B - 1
        cycles  = N // tilllcm
        start   = cycles * tilllcm
        n       = 1 + cycles * L
        if start == N: return n-1
        remain  = N - start
        i       = 1
        upperbound = 0
        print("N", N, "cycles", cycles, "start", start, "remain", remain, end=": ")
        while i < 2*L:
            tilli = i // A + i // B
            print(i, tilli, end=", ")
            if tilli < remain:
                if not upperbound:
                    i *= 2
                else:
                    i = (i + upperbound + 1) // 2
                continue
            if tilli > remain:
                upperbound = i
                i = (i * 3) // 4
                continue
            if i % A and i % B:
                upperbound = i
                i -= 1
                continue
            return cycles * L + i
                
            
S = Solution()
print(S.nthMagicalNumber(N = 1, A = 2, B = 3)) # 2
print(S.nthMagicalNumber(N = 5, A = 7, B = 5)) # 15
print(S.nthMagicalNumber(N = 4, A = 2, B = 3)) # 6
print(S.nthMagicalNumber(N = 5, A = 2, B = 4)) # 10
print(S.nthMagicalNumber(N = 3, A = 6, B = 4)) # 8
print(S.nthMagicalNumber(601,404,587))  # 143824
#print(S.nthMagicalNumber(1000000000,39999,40000))
