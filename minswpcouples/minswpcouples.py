class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        par = {}
        dis = [0 for _ in range(len(row))]
        total = 0
        for p, m in enumerate(row):
            if m % 2 == 0:
                mdash = m + 1
            else:
                mdash = m - 1
            pdash = par.get(mdash)
            if pdash is None:
                par[m] = p
                continue
            d = p - pdash
            dis[p] = -d
            dis[pdash] = d
            total += d
        print(row, dis, par)

def test(row):
    s = Solution()
    print(s.minSwapsCouples(row))

test([4,2,6,3,0,5,7,1])
#test([1,2,0,3])
#test([1,0,2,3])
