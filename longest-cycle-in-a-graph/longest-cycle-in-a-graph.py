class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = set()
        stack = []
        cycle = -1
        for s, d in enumerate(edges):
            # print("*", s, d)
            edges[s] = -1
            if d == -1: continue
            while True:
                # print(" *", s, d)
                stack.append(s)
                visited.add(s)

                if d == -1:
                    stack = []
                    break

                if d in visited:
                    c = 1
                    while c <= len(stack):
                        if stack[-c] == d:
                            cycle = max(cycle, c)
                            break
                        c += 1
                    stack = []

                s, d = d, edges[d]
                edges[s] = -1
                # print("   *", s, d, stack)
        return cycle
