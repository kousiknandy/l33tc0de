from typing import List
from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        self.graph = defaultdict(list)
        for e in edges:
            self.graph[e[0]].append(e[1])
            self.graph[e[1]].append(e[0])
        self.nodecount = [1] * N
        self.distances = [0] * N

        def node_counter(root, skip):
            for n in self.graph[root]:
                if n == skip: continue
                node_counter(n, root)
                self.nodecount[root] += self.nodecount[n]
                self.distances[root] += self.distances[n] + self.nodecount[n]

        def distance_adjust(root, skip):
            for n in self.graph[root]:
                if n == skip: continue
                self.distances[n] = self.distances[root] - self.nodecount[n] + N - self.nodecount[n]
                distance_adjust(n, root)

        node_counter(0, -1)
        print(self.nodecount)
        print(self.distances)
        distance_adjust(0, -1)
        return self.distances


S = Solution()
print(S.sumOfDistancesInTree(N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]))
print(S.sumOfDistancesInTree(7,[[1,3],[5,0],[2,5],[6,2],[4,2],[6,3]]))
            
