from typing import List
import collections

class EQgraph:
    def __init__(self):
        self.values = collections.defaultdict(list)

    def add_equation(self, n, d, v):
        self.values[n].append((d, v))
        self.values[d].append((n, 1.0/v))

    def dfs(self, s, d, v, seen):
        if s == d: return v
        for n,w in self.values[s]:
            if n in seen: continue
            seen.add(n)
            if n == d:
                return v * w
            x = self.dfs(n, d, v * w, seen)
            if x:
                return x
        return None

    def query(self, n, d):
        seen = set()
        q = self.dfs(n, d, 1.0, seen)
        return q if q else -1.0
        
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        eq = EQgraph()
        for e, v in zip(equations, values):
            eq.add_equation(e[0], e[1], v)
        result = [eq.query(q[0], q[1]) for q in queries]
        return result

S = Solution()
print(S.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
