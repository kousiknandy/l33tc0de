class Solution:
    def sumValues(self, peak, index, n):
        return ((peak * (peak+1) // 2) -
                ((peak-index-1) * (peak-index) // 2 if peak >= index else 0) +
                (peak * (peak+1) // 2) -
                ((peak-n+index-1) * (peak-n+index) // 2 if peak >= n-index else 0) -
                peak)

    def jumppeak(self, start, index, n, target):
        incr = 0
        while True:
            s = self.sumValues(start+incr, index, n)
            print("    ", start+incr, s)
            if s == target: return (start+incr)
            if s > target:
                return (incr//2 + start)
            incr = incr * 2 if incr else 1
            
    
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        peak = 0
        prevpk = 0
        while True:
            peak = self.jumppeak(peak, index, n-1, maxSum)
            print("peak: ", peak)
            if peak == prevpk: return peak
            prevpk = peak

S = Solution()
print(S.maxValue(4,2,6))    # 2
print(S.maxValue(3,2,148))  # 50
print(S.maxValue(6,1,10))   # 3
print(S.maxValue(4,0,4))    # 1
