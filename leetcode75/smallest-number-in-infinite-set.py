class SmallestInfiniteSet:

    def __init__(self):
        self.missing = set()
        self.smallest = 1

    def popSmallest(self) -> int:
        p = s = self.smallest
        self.missing.add(s)
        while s+1 in self.missing: s += 1
        self.smallest = s+1 
        return p

    def addBack(self, num: int) -> None:
        if num in self.missing: self.missing.remove(num)
        self.smallest = min(self.smallest, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
