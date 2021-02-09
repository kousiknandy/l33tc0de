from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lake_status = {}
        no_rain = []
        solution = []
        for idx, lake in enumerate(rains):
            if lake == 0:
                no_rain.append(idx)
                solution.append(None)
                continue
            solution.append(-1)
            if lake not in lake_status:
                lake_status[lake] = idx
                continue
            last_rain = lake_status[lake]
            for n in no_rain:
                if n > last_rain:
                    solution[n] = lake
                    lake_status[lake] = idx
                    no_rain.remove(n)
                    break
            else:
                return []
        for idx, s in enumerate(solution):
            if s == None:
                solution[idx] = 1
        return solution

S = Solution()
print(S.avoidFlood([1,2,3,4])) # [-1,-1,-1,-1]
print(S.avoidFlood([1,2,0,0,2,1])) # [-1,-1,2,1,-1,-1]
print(S.avoidFlood([1,2,0,1,2])) # []
print(S.avoidFlood([69,0,0,0,69])) # [-1,69,1,1,-1]
print(S.avoidFlood([10,20,20])) # []
print(S.avoidFlood([2,3,0,0,3,1,0,1,0,2,2])) # []
