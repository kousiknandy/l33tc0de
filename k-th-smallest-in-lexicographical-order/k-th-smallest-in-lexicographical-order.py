class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        counters = [0] * 9
        i = 1
        t = 0
        while t < n:
            for j in range(len(counters)):
                t += i
                if t > n:
                    counters[j] += n - t + i
                    break
                counters[j] += i
            i *= 10
        t = 1
        for j in range(len(counters)):
            t += counters[j]
            if t > k:
                t = k - t + counters[j]
                break
        print(counters, j, t, "\"", j+1, "\"")

S = Solution()
print(S.findKthNumber(680, 170))
print(S.findKthNumber(111, 58))
print(S.findKthNumber(11, 1))
print(S.findKthNumber(10, 1))

print(S.findKthNumber(605, 566))
print(S.findKthNumber(17, 10))
