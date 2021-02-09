from typing import List

class Solution:
    def greedychange(self, coins, amount, memo, depth=0):
        if len(coins) == 1:
            if amount % coins[0]:
                return False, -1
            memo[(amount,1)] = amount // coins[0]
            return True, amount // coins[0]
        if (amount, len(coins)) in memo:
            print(" "*depth, "memo:", amount, memo[(amount, len(coins))])
            return True, memo[(amount, len(coins))]
        maxlargest = amount // coins[0]
        minimum = 10000
        for i in range(maxlargest, -1, -1):
            possible, number = self.greedychange(coins[1:], amount - coins[0] * i, memo, depth+1)
            if possible:
                if i + number < minimum:
                    minimum = i + number
                    print(" "*depth, coins, amount, ":", i, "+", number, "=", minimum)
        if minimum < 10000:
            memo[(amount, len(coins))] = minimum
            return True, minimum
        return False, -1
            
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        coins = sorted(coins, reverse=True)
        _, num = self.greedychange(coins, amount, memo)
        return num

S = Solution()
print(S.coinChange([1, 2, 5], 11)) #3
print(S.coinChange([10, 9], 28)) #3
print(S.coinChange([1,2,5,10],18)) #4
print(S.coinChange([3,7,405,436], 8839)) #25
print(S.coinChange([470,18,66,301,403,112,360],8235)) #20
print(S.coinChange([288,160,10,249,40,77,314,429], 9208)) 
