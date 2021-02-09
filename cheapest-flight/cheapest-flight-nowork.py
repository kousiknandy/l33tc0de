from typing import List
from collections import deque 

class FlightGraph():
    def __init__(self, n: int, src: int):
        self.n = n
        self.flights = [[] for _ in range(n)]
        self.src = src

    def add_flight(self, flight: List[int]):
        self.flights[flight[0]].append((flight[1], flight[2]))

    def next_out(self, src: int):
        for f in self.flights[src]:
            yield f

    def __iter__(self):
        self.visited = set()
        return self

    def __next__(self):
        for f in self.next_out(self.src):
            if f[0] not in self.visited:
                self.visited.add(f[0])
                return self.next_out(f[0])

            
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        fg = FlightGraph(n, src)
        visited = set()
        cities  = deque()
        hops    = 0
        print(fg.flights)
        for f in flights:
            fg.add_flight(f)
        for c in fg:
            print(c)

S = Solution()
S.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
            
