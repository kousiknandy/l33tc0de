from typing import List
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = defaultdict(int)
        for n in nums:
            counters[n] += 1
        print(counters)
        hp = []
        for c, v in counters.items():
            if len(hp) < k:
                heapq.heappush(hp, (v, c))
            else:
                heapq.heappushpop(hp, (v, c))
            print(hp, (v,c))
        return [x[1] for x in hp]
        

S = Solution()
print(S.topKFrequent(nums = [1,1,1,2,2,3,4,4,4,4], k = 2))
