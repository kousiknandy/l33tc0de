class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = {}
        for n in nums:
            if n not in counter: counter[n] = 0
            counter[n] += 1
        ans = 0
        for n,v in counter.items():
            if n > k//2: continue
            if k % 2 == 0 and n == k//2: ans += v//2
            else: ans += min(v, counter.get(k-n,0))
        return ans
