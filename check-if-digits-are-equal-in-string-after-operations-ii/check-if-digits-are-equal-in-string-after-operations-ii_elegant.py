class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def binoseq(n):
            c = 1
            yield 1
            for i in range(n):
                c = c * (n-i) // (i+1)
                yield c
        n = len(s)
        a =[int(x) for x in s]
        fd = sum(map(lambda x: x[0]*x[1], zip(a[:n-1],binoseq(n-2)))
        ld = sum(map(lambda x: x[0]*x[1], zip(a[1:],binoseq(n-2))))
        return fd % 10 == ld % 10
