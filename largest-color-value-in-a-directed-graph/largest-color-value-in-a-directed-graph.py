from collections import defaultdict
class Solution:
    def dfs(self, source, colors, adjacency_list, totalcolors):
        if len(totalcolors[source]) != 0: return totalcolors[source]
        totalcolors[source][colors[source]] = 1
        for n in adjacency_list[source]:
            cols = self.dfs(n, colors, adjacency_list, totalcolors)
            for c,v in cols.items():
                if c == colors[source]: v+= 1
                if c not in totalcolors[source]: totalcolors[source][c] = 0
                totalcolors[source][c] = max(totalcolors[source][c], v)
        return totalcolors[source]

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        indegrees = defaultdict(int)
        adjacency = defaultdict(list)
        totalcolor = defaultdict(dict)
        for s,d in edges: 
            if s == d: return -1
            indegrees[d] += 1
            adjacency[s].append(d)
            if s in adjacency[d]: return -1
        for s in adjacency: indegrees[s]
        starts = [s for s,d in indegrees.items() if d == 0]
        if len(edges) == 0: return 1
        if len(starts) == 0: return -1
        for s in starts:
            self.dfs(s, colors, adjacency, totalcolor)
        # print(totalcolor)
        return max([max([v for v in totalcolor[s].values()]) for s in starts])
