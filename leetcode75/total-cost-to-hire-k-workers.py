import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if len(costs) <= 2*candidates:
            return sum(heapq.nsmallest(k,costs))
        indxcost = list(zip(costs,range(len(costs))))
        h1 = indxcost[:candidates]
        h2 = indxcost[-candidates:]
        heapq.heapify(h1)
        heapq.heapify(h2)
        p1 = candidates
        p2 = len(costs)-candidates-1
        tot = 0
        while p1 <= p2 and k:
            if h1[0] <= h2[0]:
                m,_ = heapq.heapreplace(h1, (costs[p1],p1))
                p1 += 1
            else:
                m,_ = heapq.heapreplace(h2, (costs[p2],p2))
                p2 -= 1
            tot += m
            k -= 1
        if k:
            h = heapq.merge(h1,h2)
            tot += sum(x[0] for x in heapq.nsmallest(k,h))
        return tot
