from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key=lambda x: x[1])
        last = 0
        count = 0
        for event in events:
            if last < event[0]:
                count += 1
                last = event[0]
            elif last < event[1]:
                count += 1
                last += 1
            #print(event, last, count)
        return count


S = Solution()
print(S.maxEvents(events = [[1,4],[4,4],[2,2],[3,4],[1,1]])) #4
#print(S.maxEvents(
print(S.maxEvents(events = [[1,2],[2,3],[3,4]])) #3
print(S.maxEvents([[1,2],[2,3],[3,4],[1,2]])) #4
print(S.maxEvents([[1,100000]])) #1
print(S.maxEvents(events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]])) #7
print(S.maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]]))
