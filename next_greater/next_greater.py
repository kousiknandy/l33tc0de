from collections import deque 

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        st = deque()
        solution = [None for _ in range(len(A))]
        for idx, val in enumerate(A):
            while True:
                try:
                    t = st.pop()
                except IndexError:
                    st.append((val, idx))
                    break
                if t[0] >= val:
                    st.append(t)
                    st.append((val, idx))
                    break
                solution[t[1]] = val
        while True:
            try:
                t = st.pop()
                solution[t[1]] = -1
            except IndexError:
                break
        return solution

S = Solution()
print(S.nextGreater([4, 5, 2, 10])) # 5, 10, 10, -1
print(S.nextGreater([3, 2, 1])) # -1 -1 -1

