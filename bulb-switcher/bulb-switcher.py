class Solution:
    def bulbSwitch(self, n: int) -> int:
        def isqrt(n):
            x = n
            y = (x + 1) // 2
            while y < x:
                x = y
                y = (x + n // x) // 2
            return x

        p = isqrt(n)
        return p
