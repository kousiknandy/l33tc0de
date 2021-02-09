from typing import List
from collections import defaultdict
from re import split

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_map = defaultdict(int)
        result   = []
        for name in names:
            subscript = name_map[name]
            name_map[name] = subscript + 1
            parts = split(r"\((\d+)\)$", name)
            if len(parts) > 1:
                subscript2 = name_map[parts[0]]
                if subscript2:
                    if subscript2 >= int(parts[1]):
                        name_map[parts[0]] = subscript2 + 1
            if subscript:
                name += "(" + str(subscript) + ")"
                name_map[name] = 1
            result.append(name)
        return result

S = Solution()

print(S.getFolderNames(names = ["pes","fifa","gta","pes(2019)"]))
print(S.getFolderNames(names = ["gta","gta(1)","gta","avalon"]))
print(S.getFolderNames(names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]))
print(S.getFolderNames(names = ["wano","wano","wano","wano"]))
print(S.getFolderNames(names = ["kaido","kaido(1)","kaido","kaido(1)"]))
print(S.getFolderNames(["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]))
