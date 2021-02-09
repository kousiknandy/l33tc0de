from typing import List

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory = sorted(inventory, reverse=True)
        cuvalues  = [None] * len(inventory)
        idx = 0
        gsz = 1
        ball = 0
        totalvalue = 0
        value = 0
        while idx < len(inventory):
            val = inventory[idx]
            if idx < len(inventory) - 1:
                if inventory[idx + 1] == val:
                    cuvalues[idx] = (value, totalvalue, val, 0,  gsz, ball)
                    gsz += 1
                    idx += 1
                    continue
                value = ((val * (val + 1) // 2) - (inventory[idx+1] * (inventory[idx+1] + 1) // 2)) * gsz
                diff  = val - inventory[idx+1]
            else:
                value = (val * (val + 1) // 2) * gsz
                diff  = val
            ball += diff * gsz
            totalvalue += value
            cuvalues[idx] = (value, totalvalue, val, diff,  gsz, ball)
            if ball >= orders:
                totalvalue -= value
                diff = (diff * gsz) - (ball - orders)
                ful  = diff // gsz
                part = diff % gsz
                value= ((val*(val+1)//2) - ((val-ful+1)*(val-ful)//2)) * gsz
                value+= (val - ful)*part
                totalvalue += value
                print(value)
                break
            idx += 1
            gsz += 1
        print(totalvalue, cuvalues)
        return totalvalue % 1000000007

S = Solution()
print(S.maxProfit([10, 8, 5, 3], 16))
print(S.maxProfit([10, 8, 5, 5, 5, 3], 16))
print(S.maxProfit(inventory = [2,8,4,10,6], orders = 20))
print(S.maxProfit(inventory = [3,5], orders = 6))
print(S.maxProfit(inventory = [1000, 1000], orders = 2))
print(S.maxProfit(inventory = [1000000000], orders = 1000000000))
