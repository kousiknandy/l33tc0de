from functools import reduce

class Solution:
    def isHappy(self, n: int) -> bool:
        mem = {n: True}
        digits = lambda x: map(int, str(x))
        sqrsum = n
        while True:
            sqrsum = reduce(lambda x, y: x + y*y, digits(sqrsum), 0)
            print(sqrsum)
            if sqrsum == 1: return True
            if sqrsum in mem: return False
            mem[sqrsum] = True

S = Solution()
print(S.isHappy(7))
