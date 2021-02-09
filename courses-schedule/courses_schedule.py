from typing import List
import collections

class Solution:
    def dfs(self, coursegraph, node, visited, current):
        visited[node] = current[node] = True
        for n in coursegraph[node]:
            if not visited[n]:
                if self.dfs(coursegraph, n, visited, current):
                    return True
            elif current[n]:
                return True
        current[node] = False
        return False
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursegraph = collections.defaultdict(list)
        visited = [False] * numCourses
        current = [False] * numCourses
        for p in prerequisites:
            coursegraph[p[0]].append(p[1])
        for i in range(numCourses):
            if not visited[i]:
                if self.dfs(coursegraph, i, visited, current):
                    return False
        return True
    
