import collections
from typing import List

class Solution:
    def ufind(self, x):
        if self.parentset[x] == x: return x
        return self.ufind(self.parentset[x])
    
    def uunion(self, x, y):
        xp = self.ufind(x)
        yp = self.ufind(y)
        if xp < yp:
            self.parentset[xp] = yp
        else:
            self.parentset[yp] = xp
        # print("   ", x, y, xp, yp)
    
    def equationsPossible(self, equations: List[str]) -> bool:
        self.parentset = [i for i in range(26)]
        self.eqgraph = collections.defaultdict(list)
        for eq in equations:
            if eq[1] == "=":
                l = ord(eq[0]) - ord("a")
                r = ord(eq[3]) - ord("a")
                self.eqgraph[l].append(r)
                self.eqgraph[r].append(l)
        for i,eqs in self.eqgraph.items():
            for e in eqs:
                # print(i,e, end=", ")
                self.uunion(i, e)
        # print(self.parentset)
        for eq in equations:
            if eq[1] == "!":
                l = ord(eq[0]) - ord("a")
                r = ord(eq[3]) - ord("a")
                if self.ufind(l) == self.ufind(r):
                    return False
        return True

S = Solution()
print(S.equationsPossible(["a==b","b==c","a==c","c==c","b==d","x!=z"]))
