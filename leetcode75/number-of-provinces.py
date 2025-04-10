class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(parents, x):
            while x != parents[x]:
                x = parents[x] = parents[parents[x]]
            return x
        
        def union(parents, sizes, x, y):
            r1 = find(parents, x)
            r2 = find(parents, y)
            if r1 == r2: return 
            if sizes[r1] <= sizes[r2]: r1, r2 = r2, r1
            parents[r2] = r1
            sizes[r1] += sizes[r2]
            sizes[r2] = 0
            

        n = sets = len(isConnected[0])
        parents = [x for x in range(n)]
        sizes = [1] * n
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    union(parents,sizes,i,j)
        return len([x for x in sizes if x])
