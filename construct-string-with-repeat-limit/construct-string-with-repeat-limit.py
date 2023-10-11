from collections import Counter

class Solution:
    def nextstr(self, c, r):
        last = None
        while True:
            if len(c) == 0: return
            if c[0][0] != last:
                l = min(c[0][1], r)
                yield c[0][0] * l
                last = c[0][0]
                if c[0][1] - l == 0:
                    del c[0]
                    continue
                c[0] = (c[0][0], c[0][1] - l)
            if len(c) < 2: return 
            yield c[1][0]
            last = c[1][0]
            if c[1][1] == 1:
                del c[1]
            else:
                c[1] = (c[1][0], c[1][1] - 1)

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        c = Counter(s)
        c = [(k,v) for k,v in sorted(c.items(),reverse=True)]
        res = "".join(self.nextstr(c, repeatLimit))
        return res
