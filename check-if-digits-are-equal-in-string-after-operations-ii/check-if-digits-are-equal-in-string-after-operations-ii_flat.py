class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        a =[int(x) for x in s]
        fd = ld = 0
        binc = 1
        for i in range(n-1):
            fd += (a[i]*binc) % 10
            ld += (a[i+1]*binc) % 10
            binc = binc * (n-2-i) // (i+1)
        return fd % 10 == ld % 10
