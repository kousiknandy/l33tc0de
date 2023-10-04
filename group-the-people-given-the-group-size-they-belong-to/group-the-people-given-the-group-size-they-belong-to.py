class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        grps = defaultdict(list)
        for i, g in enumerate(groupSizes):
            grps[g].append(i)
        res = []
        for s, l in grps.items():
            res += [l[i : i+s] for i in range(0, len(l), s)]
        return res
