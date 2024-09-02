import re

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        prex = r"(?P<SUB>(?<=\()\w+(?=\))?)|(?P<LIT>\w)"
        know = {k[0]: k[1] for k in knowledge}
        res = ""
        for tok in re.finditer(prex, s):
            v = tok.group()
            res += v if tok.lastgroup == "LIT" else know.get(v, "?")
        return res
