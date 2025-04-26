class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0]) 
        s = intervals[0][0]
        e = intervals[0][1]
        deleted = 0
        for i in range(1, len(intervals)):
            s1, e1 = intervals[i]
            if s1 >= e:
                s, e = s1, e1
                continue
            if e1 >= e:
                deleted += 1
                continue
            s, e = s1, e1
            deleted += 1
        return deleted 

