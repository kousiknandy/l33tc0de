class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combs = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def letters(prefix, suffix, combs):
            if len(suffix) == 0:
                if prefix:
                    yield prefix
                return
            d, suffix = suffix[0], suffix[1:]
            for c in combs[d]:
                yield from letters(prefix + c, suffix, combs)

        return list(letters("", digits, combs))
