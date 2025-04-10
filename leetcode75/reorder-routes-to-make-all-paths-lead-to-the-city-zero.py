class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = {}
        for s, d in connections:
            if s not in adj: adj[s] = []
            if d not in adj: adj[d] = []
            adj[s].append((d,True))
            adj[d].append((s,False))
        
        def traverse(root, parent, adj):
            for d, out in adj[root]:
                if d == parent: continue
                if out: yield out
                yield from traverse(d, root, adj)

        def count(root, parent, adj):
            c = 0
            for d, out in adj[root]:
                if d == parent: continue
                if out: c += 1
                c += count(d, root, adj)
            return c

        #counter
        return count(0, None, adj)

        # generator, TLEs
        rev = 0
        for r in traverse(0, None, adj):
            if r: rev += 1
        return rev
