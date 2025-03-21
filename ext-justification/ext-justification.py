class Solution:
    def fullJustify(self, words: List[str], maxwidth: int) -> List[str]:
        wl = []
        l = 0
        sl = []
        res = []
        for w in words:
            if l+len(w) == maxwidth:
                wl.append(w)
                l = " ".join(wl)
                res.append(l)
                wl = []
                l = 0
                sl = []
                continue
            if l+len(w) > maxwidth:
                wc = len(wl)
                lc = l - wc
                sp = maxwidth - lc
                if wc == 1:
                    l = wl[0] + " "*sp
                else:
                    ms = sp // (wc-1)
                    es = sp % (wc-1)
                    sp = [" "*ms for _ in range(wc-1)]
                    for _ in range(es): sp[_] += " "
                    l = ""
                    for i,ww in enumerate(wl):
                        l += ww
                        l += sp[i] if i < wc-1 else ""
                res.append(l)
                wl = []
                l = 0
            wl.append(w)
            l += len(w) + 1
        if wl:
            l = " ".join(wl)
            l += " "*(maxwidth - len(l))
            res.append(l)
        return res
                
