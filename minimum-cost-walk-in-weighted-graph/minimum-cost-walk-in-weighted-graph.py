class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        def find(pw, s):
            while s != pw[s]:
                pw[s] = pw[pw[s]]
                s = pw[s]
            return s

        def union(pw, s, t):
            r1 = find(pw, s)
            r2 = find(pw, t)
            if r1 == r2:  return 
            if r1 < r2:
                pw[r2] = r1
            else:
                pw[r1] = r2

        pw = [i for i in range(n)]
        for s,t,w in edges:
            union(pw,s,t)
        we = [-1] * n
        for s,t,w in edges:
            p = find(pw,s)
            we[p] = we[p] & w
            p = find(pw,t)
            we[p] = we[p] & w
        # print(pw,we,sep="\n")
        res = []
        for s,t in query:
            ps = find(pw,s)
            pt = find(pw,t)
            if ps == pt:
                p = find(pw,ps) 
                # print(s,t,pt,p,we[p])
                res.append(we[p])
            else: res.append(-1)
        return res
