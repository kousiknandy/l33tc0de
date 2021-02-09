from typing import List
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)
        counters = [0] * 26
        for t in tasks:
            idx = ord(t) - ord("A")
            counters[idx] += 1
        counters = sorted(counters, reverse=True)
        counters = [x for x in counters if x]
        #print(counters)
        sliding_window = deque()
        for i in range(n): sliding_window.append(None)
        interval = 0
        while any(counters):
            print(sliding_window, counters)
            for i in range(len(counters)):
                if i in sliding_window or counters[i] == 0:
                    continue
                sliding_window.popleft()
                sliding_window.append(i)
                interval += 1
                counters[i] -= 1
                break
            else:
                sliding_window.popleft()
                sliding_window.append(None)
                interval += 1
            #counters = sorted(counters, reverse=True)
        return interval

S = Solution()
print(S.leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2))
print(S.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
print(S.leastInterval(tasks = ["A","A","A","B","B","B"], n = 0))
print(S.leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], 2))
