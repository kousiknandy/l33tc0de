class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        for edge, val in zip(equations, values):
            if edge[0] not in adj: adj[edge[0]] = []
            if edge[1] not in adj: adj[edge[1]] = []
            adj[edge[0]].append((edge[1], val))
            adj[edge[1]].append((edge[0], 1/val))
        
        res = []
        for num, den in queries:
            if num not in adj or den not in adj:
                res.append(-1.0)
                continue
            visited = set()
            bfsq = deque()
            bfsq.append((num,1.0))
            while len(bfsq) > 0:
                n, w = bfsq.popleft()
                if n in visited: continue
                else: visited.add(n)
                if n == den:
                    res.append(w)
                    break
                for m,x in adj[n]:
                    bfsq.append((m,w*x))
            else:
                res.append(-1.0)

        return res
