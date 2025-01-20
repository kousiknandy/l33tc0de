class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        sq = [None for _ in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            p = []
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    p.append((sq[j][0]+1,sq[j][1]))
            p.append((1,1))
            p.sort(reverse=True)
            m = p[0][0]
            s = 0
            for q in p:
                if q[0] != m: break
                s += q[1]
            sq[i] = (m,s)
        m = max(sq)
        s = 0
        for q in sq:
            if q[0] != m[0]: continue
            s += q[1]
        return s
