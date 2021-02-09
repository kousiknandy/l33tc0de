class Solution:
    def majority_candidate(self, A):
        count = 0
        candidate_index = 0
        for i in range(len(A)):
            count += 1 if A[i] == A[candidate_index] else -1
            if count == 0:
                candidate_index = i
                count = 1
        return candidate_index

    def verify_candidate(self, A, candidate_index):
        count = 0
        for i in range(len(A)):
            if A[i] == A[candidate_index]:
                count += 1
        return count > (len(A) // 2)
        
        
    def majorityElement(self, A):
        cand = self.majority_candidate(A)
        if self.verify_candidate(A, cand):
            return A[cand]
        return -1


S = Solution()
print(S.majorityElement([1,2,1,3,1,4,1,1]))
print(S.majorityElement([1,2,1,3,1,4,0,0]))
print(S.majorityElement([1,1,1,1,1,1,1,1]))
print(S.majorityElement([0,1,0,1,0,1,0,1]))

