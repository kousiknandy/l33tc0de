class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        def bit(n):
            p = 1 << 31
            while p:
                yield 1 if n & p else 0
                p >>= 1
            return 0
        ba, bb, bc = bit(a), bit(b), bit(c)
        flip = 0
        for c1 in bc:
            a1 = next(ba)
            b1 = next(bb)
            if c1 and (a1 or b1): continue
            if not c1 and (not a1 and not b1): continue
            if c1: flip += 1
            else: flip += 2 if (a1 and b1) else 1
        return flip
