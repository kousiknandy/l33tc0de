class Solution:
    def nextquad(self, s, q):
        # print(" "*q, s, q)
        if len(s) == 0: return None
        if q == 3:
            if s == "0": return [s]
            if s[0] == "0" or int(s) > 255: return None
            return [s]
        if s[0] == "0":
            r = None
            t = self.nextquad(s[1:], q+1)
            if t:
                r = ["0." + p for p in t if p]
            return r
        r = []
        for i in range(1, len(s)+1):
            w = s[:i]
            if int(w) > 255: break
            # print(w, end=".")
            t = self.nextquad(s[i:], q+1)
            if t:
                r += [w + "." + p for p in t if p]
        return r

    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.nextquad(s, 0)
