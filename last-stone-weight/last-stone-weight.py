class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        s1 = 0
        try:
            while True:
                s1 = heapq.heappop(stones)
                s2 = heapq.heappop(stones)
                if s1 == s2:
                    s1 = s2 = 0
                    continue
                heapq.heappush(stones, s1-s2)
        except IndexError:
            return -s1
