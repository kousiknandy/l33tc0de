class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(parent, x):
            if x != parent[x]:
                parent[x] = find(parent, parent[x])
            return parent[x]
        def union(parent, x, y):
            r1 = find(parent,x)
            r2 = find(parent,y)
            if r1 == r2: return
            if r1 < r2: parent[r2] = r1
            else: parent[r1] = r2
        degrees = [0] * n
        parent = [i for i in range(n)]
        components = defaultdict(list)
        for s,t in edges:
            union(parent,s,t)
            degrees[s] += 1
            degrees[t] += 1
        for s in range(n):
            p = find(parent,s)
            components[p].append(s)
        ans = 0
        for c in components:
            if all(degrees[x] == len(components[c])-1 for x in components[c]):
                ans += 1
        return ans
