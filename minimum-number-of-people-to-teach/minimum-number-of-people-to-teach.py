from typing import List
from collections import defaultdict

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        def common_language(a ,b):
            i = j = 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]: return a[i]
                elif a[i] > b[j]: j += 1
                elif a[i] < b[j]: i += 1
            return None
        languages = [sorted(l) for l in languages]
        need_lang = defaultdict(list)
        for f in friendships:
            u = f[0]-1
            v = f[1]-1
            if common_language(languages[u], languages[v]) is None:
                need_lang[u].append(v)
                need_lang[v].append(u)
        lang_counter = [0] * n
        for v in need_lang:
            for l in languages[v]:
                lang_counter[l-1] += 1
        most_common = lang_counter.index(max(lang_counter)) + 1
        result = 0
        for v in need_lang:
            if most_common not in languages[v]:
                result += 1
        return result

S = Solution()
print(S.minimumTeachings(n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]))  #1
print(S.minimumTeachings(n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]))  #2
