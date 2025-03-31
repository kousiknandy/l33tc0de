class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            stack.append(a)
            while len(stack) >= 2:
                a, b = stack[-1], stack[-2]
                if a < 0 and  b > 0:
                    if abs(a) < abs(b): 
                        stack.pop()
                        break
                    stack.pop()
                    stack.pop()
                    if abs(a) > abs(b):
                        stack.append(a)
                else:
                    break
        return stack
