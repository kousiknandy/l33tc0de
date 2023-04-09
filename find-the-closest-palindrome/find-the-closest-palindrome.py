class Solution:
    def gen_pal(self, n):
        mid = len(n) // 2 - 1
        d = n[mid+1] if len(n) % 2 else ""
        lhs = n[:mid+1]
        p1 = lhs + d + lhs[::-1]
        return p1

    def nearestPalindromic(self, n: str) -> str:
        if int(n) <= 10: return str(int(n)-1)
        if int(n) == 11: return "9"
        k = int(n)
        while k//10 and not k%10: k//=10
        if k == 1: return str(int(n)-1)
        msk = len(n) // 2 + 1
        mask = 10**(msk-1)
        p1 = self.gen_pal(n)
        p2 = str(int(n) + mask)
        p3 = str(int(n) - mask)
        p2 = self.gen_pal(p2)
        p3 = self.gen_pal(p3)
        # print(n, p1,  p2, p3, sep=",")
        d1 = abs(int(n) - int(p1)), p1
        d2 = abs(int(n) - int(p2)), p2
        d3 = abs(int(n) - int(p3)), p3
        d = sorted([d1, d2, d3])
        if d[0][0] == 0:
            if d[1][0] < d[2][0]: return d[1][1]
            if int(d[1][1]) < int(d[2][1]):
                return d[1][1]
            return d[2][1]
        if d[0][0] < d[1][0]: return d[0][1]
        if int(d[0][1]) < int(d[1][1]):
            return d[0][1]
        return d[1][1]
