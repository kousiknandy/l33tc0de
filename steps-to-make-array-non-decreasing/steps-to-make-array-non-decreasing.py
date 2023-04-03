class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        for n in reversed(nums):
            # print(stack)
            if len(stack) < 1:
                stack.append((n, 0))
                continue
            t, c = stack[-1]
            if n <= t:
                stack.append((n, 0))
                continue
            pc = 0
            while t < n:
                t, c = stack.pop()
                pc += 1 
                pc = max(pc, c)
                if len(stack) == 0:
                    break
                t, c2 = stack[-1]
            stack.append((n, pc))
        mx = 0
        for t, c in stack:
            mx = max(c, mx)
        # print("*", stack)
        return mx
