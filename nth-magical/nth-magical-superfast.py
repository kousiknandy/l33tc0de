class Solution:
    def tilllcm(self, a, b):
        l = math.lcm(a, b)
        return l, (l//a) + (l//b) - 1

    def nth(self, n, a, b):
        if n == 0: return 0
        x, y = (b*n)//(a+b), (a*n)//(a+b)
        return min((x+1)*a, (y+1)*b)

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        l, c = self.tilllcm(a, b)
        f, p = divmod(n, c)
        # print(l,c,f,p)
        return (f*l + self.nth(p, a, b))%(1000000007)
