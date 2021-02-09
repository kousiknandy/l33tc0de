class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        primes = bytearray(n)
        for i in range(2, int(n**0.5)+1):
            if primes[i]: continue
            j = i * i
            while j < n:
                primes[j] = 1
                j += i
        count = 0
        #print(primes)
        for i in range(n):
            if primes[i] == 0: count += 1
        return count - 2

S = Solution()
print(S.countPrimes(2))     #3
print(S.countPrimes(6))     #3
print(S.countPrimes(10))    #4
print(S.countPrimes(22))    #8
print(S.countPrimes(100))   #25
print(S.countPrimes(1000))  #168
print(S.countPrimes(100000))#9592 

