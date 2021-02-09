from typing import List

class Solution:
    def nearest_heater(self, house, heaters):
        l = 0
        r = len(heaters) - 1
        if house < heaters[l]:
            return heaters[l] - house
        if house > heaters[r]:
            return house - heaters[r]
        while l < r:
            m = (l + r) // 2
            heat = heaters[m]
            if heat == house:
                return 0
            elif heat > house:
                r = m
            elif heat < house:
                l = m + 1
        return min(abs(house - heaters[l]), abs(house - heaters[l-1]))
            
            
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters = sorted(heaters)
        dist    = (self.nearest_heater(house, heaters) for house in houses)
        return max(dist)


S = Solution()
# print(S.nearest_heater(5, [1, 3, 4, 7, 9, 11, 12, 16, 17, 20])) # 1 (4-5)
# print(S.nearest_heater(11, [1, 3, 4, 7, 9, 11, 12, 16, 17, 20])) # 0
# print(S.nearest_heater(13, [1, 3, 4, 7, 9, 11, 12, 16, 17, 20])) # 1 (12-13)
# print(S.nearest_heater(20, [1, 3, 4, 7, 9, 11, 12, 16, 17, 22])) # 2, (22-20)
# print(S.nearest_heater(10, [1, 3, 4, 7, 9, 11, 12, 16, 17, 20])) # 1, (9-10)/(10-11)

print(S.findRadius(houses = [1,2,3,4], heaters = [1,4])) # 1
print(S.findRadius(houses = [1,2,3], heaters = [2]))     # 1
print(S.findRadius(houses = [1,5], heaters = [2]))       # 3
