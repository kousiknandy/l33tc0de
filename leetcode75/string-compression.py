class Solution:
    def compress(self, chars: List[str]) -> int:
        def digits(n):
            d = []
            while n:
                n, r = divmod(n,10)
                d = [str(r)] + d
            return d
        cur, run, s = None, 0, []
        for c in chars:
            if cur is None: cur = c
            if cur == c: 
                run += 1
                continue
            s.append(cur)
            if run > 1: s.extend(digits(run))
            cur = c
            run = 1
        s.append(cur)
        if run > 1: s.extend(digits(run))
        for i,c in enumerate(s):
            chars[i] = c
        return len(s)
