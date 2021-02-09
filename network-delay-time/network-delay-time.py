from typing import List
import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        network = collections.defaultdict(list)
        for t in times:
            network[t[0]].append((t[1], t[2]))
        delaymap = [0] + [2**32] * N
        bfsq = collections.deque()
        bfsq.append((K, 0))
        while len(bfsq) > 0:
            node, delay = bfsq.popleft()
            if delay >= delaymap[node]:
                continue
            delaymap[node] = delay
            for n in network[node]:
                bfsq.append((n[0], n[1]+delay))
        maxdelay = max(delaymap)
        return -1 if maxdelay == 2**32 else maxdelay
    
