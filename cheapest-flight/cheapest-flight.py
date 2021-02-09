from typing import List
from collections import deque

class FlightGraph():
    def __init__(self, n: int, src: int, dst: int, maxdep: int):
        self.n = n
        self.flights = [[] for _ in range(n)]
        self.src = src
        self.dst = dst
        self.visited = set()
        self.maxdep = maxdep
        self.mincost = -1

    def add_flight(self, flight: List[int]):
        self.flights[flight[0]].append((flight[1], flight[2]))

    def dfsrecurse(self, src: int, depth: int, cost: int):
        c = cost
        for v in self.flights[src]:
            if v[0] == self.src:  # in self.visited:
                continue
            self.visited.add(v[0])
            cost = c + v[1]
            print(" " * depth, v[0], cost)
            if self.mincost > 0 and cost > self.mincost:
                continue
            if v[0] == self.dst:
                if self.mincost == -1 or self.mincost > cost:
                    self.mincost = cost
                    continue
            if depth >= self.maxdep:
                continue
            self.dfsrecurse(v[0], depth+1, cost)
        
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        fg = FlightGraph(n, src, dst, K)
        for f in flights:
            fg.add_flight(f)
        print(fg.flights)
        fg.dfsrecurse(src, 0, 0)
        print(fg.mincost)
        return fg.mincost

S = Solution()
S.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
S.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)
S.findCheapestPrice(5,[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]],2,1,1)
S.findCheapestPrice(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], 0, 2, 2)
S.findCheapestPrice(17,
                    [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]],
                    13,
                    4,
                    13)
