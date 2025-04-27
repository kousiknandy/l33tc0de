class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        def bit(n, p):
            while p:
                yield n % 2
                p //= 2
                n //= 2
            return 0

        ba, bb, bc = bit(a, max(a, b, c)), bit(b, max(a, b, c)), bit(c, max(a, b, c))
        flip = 0
        for c1 in bc:
            a1 = next(ba)
            b1 = next(bb)
            if c1 and (a1 or b1):
                continue
            if not c1 and (not a1 and not b1):
                continue
            if c1:
                flip += 1
            else:
                flip += 2 if (a1 and b1) else 1
        return flip
