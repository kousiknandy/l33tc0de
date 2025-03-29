class Solution:
    def maxArea(self, height: List[int]) -> int:
        def nextwall(height, direction):
            cp = 0 if direction else len(height)-1
            dir = 1 if direction else -1
            while cp >= 0 and cp <= len(height)-1:
                yield cp, height[cp]
                if cp+dir < 0 or cp+dir >= len(height): break
                while height[cp] >= height[cp+dir]:
                    cp += dir
                    if cp+dir < 0 or cp+dir >= len(height): break
                cp += dir

        lw, rw = nextwall(height, True), nextwall(height, False)
        cl,clh = next(lw)
        cr,crh = next(rw)
        watervol = min(clh,crh) * (cr - cl)
        nl,nr = None, None 
        while cr-cl >= 1:
            watervol = max(watervol, min(clh,crh) * (cr - cl))
            try: 
                if nl is None: nl,nlh = next(lw)
            except StopIteration: pass
            try: 
                if nr is None: nr,nrh = next(rw)
            except StopIteration: pass
            print(watervol,cl,cr,nl,nr)
            if nl is not None:
                newwatervol = min(nlh,crh) * (cr - nl)
                if newwatervol >= watervol:
                    watervol = newwatervol
                    cl,clh = nl,nlh
                    nl = None
            if nr is not None:
                newwatervol = min(clh,nrh) * (nr - cl)
                if newwatervol >= watervol:
                    watervol = newwatervol
                    cr,crh = nr,nrh
                    nr = None
            if nl and nr: break
            if not nl and not nr: break
        return watervol
