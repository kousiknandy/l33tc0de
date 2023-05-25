class Solution:
    def gcd(x, y):
        while y: x, y = y, x % y
        return x

    def accsum(self, s):
        return sum([p[0]*p[1] for p in zip(s, range(1,len(s)+1))])

    def popsum(self, heap, seen, n):
        c = []
        r = []
        if len(seen) == n: return []
        try:
            g, i, j = heapq.heappop(heap)
        except IndexError:
            return []
        if i not in seen and j not in seen:
            c.insert(0, -g)
            seen += [i, j]
        c = self.popsum(heap, seen, n) + c
        # print(c)
        return c


    def maxScore(self, nums: List[int]) -> int:
        h = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                h.append((-gcd(nums[i], nums[j]), i, j))
        heapq.heapify(h)
        s = self.popsum(h, [], len(nums))
        return self.accsum(s)
