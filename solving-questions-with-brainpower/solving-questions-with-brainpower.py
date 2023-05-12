class Solution:
    @lru_cache
    def indexpoints(self, idx):
        if idx >= len(self.questions): return 0
        p1 = self.questions[idx][0] + self.indexpoints(idx + self.questions[idx][1] + 1)
        p2 = self.indexpoints(idx+1)
        return max(p1, p2)

    def mostPoints(self, questions: List[List[int]]) -> int:
        self.questions = questions
        return self.indexpoints(0)
