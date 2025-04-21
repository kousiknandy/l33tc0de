class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for d, t in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < t:
                t1, d1 = stack.pop()
                ans[d1] = d - d1
            stack.append((t, d))
        return ans
