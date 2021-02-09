class Solution:
    def getMoneyAmount(self, n: int) -> int:
        memo = {}
        
        def cost(start, end, depth=0):
            #print("\n", "   "*depth, start, end, end=": ")
            if end - start == 2:
                #print(end-1)
                return end - 1
            if end - start == 1:
                #print(start)
                return start
            if end - start == 0:
                return 0
            if mincost := memo.get((start, end)):
                return mincost
            else:
                mincost = 2**32-1
            for i in range(start+1, end):
                child_cost = max(cost(start, i-1, depth+1), cost(i+1,end, depth+1))
                total_cost = i + child_cost
                mincost    = min(mincost, total_cost)
                #print(i, total_cost, mincost, end=", ")
            #print(mincost)
            memo[(start, end)] = mincost
            return mincost
        
        return cost(1, n)


S = Solution()
print(S.getMoneyAmount(45))
