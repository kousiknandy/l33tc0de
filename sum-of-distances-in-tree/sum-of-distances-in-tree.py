from typing import List
from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        self.dist = [[10000 for _ in range(N)] for _ in range(N)]
        for e in edges:
            self.dist[e[0]][e[1]] = 1
            self.dist[e[1]][e[0]] = 1
        for i in range(N):
            for j in range(N):
                if i == j:
                    self.dist[i][j] = 0
                    continue
                for k in range(N):
                    self.dist[i][j] = min(self.dist[i][j], self.dist[i][k]+self.dist[k][j])
                    self.dist[j][i] = self.dist[i][j]
        print(self.dist)
        return [sum(x) for x in self.dist]

S = Solution()
print(S.sumOfDistancesInTree(N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]))
print(S.sumOfDistancesInTree(7,[[1,3],[5,0],[2,5],[6,2],[4,2],[6,3]]))
