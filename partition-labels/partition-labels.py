from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        index = lambda c: ord(c) - ord('a')
        end = [-1] * 26
        for i, c in enumerate(S):
            p = index(c)
            end[p] = i
        parts = []
        p_begin = 0
        p_end = end[index(S[p_begin])]
        for i, c in enumerate(S):
            if i == p_end:
                parts.append(p_end - p_begin + 1)
                if i < len(S)-1:
                    p_begin = i + 1
                    p_end = end[index(S[p_begin])]
                continue
            p_end = max(p_end, end[index(c)])
        return parts

S = Solution()
print(S.partitionLabels("ababcbacadefegdehijhklij"))  # 9,7,8
