class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(parents, x):
            while x != parents[x]:
                x = parents[x] = parents[parents[x]]
            return x

        def union(parents, x, y, sets):
            r1 = find(parents,x)
            r2 = find(parents,y)
            if r1 == r2: return sets
            if r1 < r2: parents[r2] = r1
            else: parents[r1] = r2
            return max(1, sets-1)

        sets = n = len(isConnected[0])
        parents = [x for x in range(sets)]
        for i in range(n):
            for j in range(i+1, n):
                # print(i,j, "*" if isConnected[i][j] else "")
                if isConnected[i][j]:
                    sets = union(parents,i,j,sets)
        return sets
