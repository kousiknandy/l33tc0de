class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        exa, exb, dups = set(), set(), set()
        for n in nums1: exa.add(n)
        for n in nums2:
            if n in exa: 
                exa.remove(n)
                dups.add(n)
            elif n not in dups: exb.add(n)
        return [list(exa), list(exb)]
