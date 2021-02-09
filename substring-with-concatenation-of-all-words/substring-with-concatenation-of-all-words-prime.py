from typing import List
import itertools

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

def rolling_product(st, l=None, r=None, ckproduct=1):
    p = ckproduct
    if l and r:
        return ckproduct * primes[ord(r)-ord('a')] // primes[ord(l)-ord('a')]
    for s in st:
        p *= primes[ord(s)-ord('a')]
    return p

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        target_hashes = []
        target_strings = []
        for perm in itertools.permutations(words):
            s1 = 1
            for x in perm:
                s1 = rolling_product(x, ckproduct=s1)
            target_hashes.append(s1)
            target_strings.append("".join(perm))
            print(perm, ":", s1)
        if len(words) == 0:
            return []
        fullen = len(words) * len(words[0])
        if len(s) < fullen:
            return []
        adler = 1
        solution = []
        for win in range(len(s) - fullen + 1):
            if win == 0:
                adler = rolling_product(s[win:(win+fullen)])
            else:
                adler = rolling_product(s[win:(win+fullen-1)], s[win-1], \
                                        s[win+fullen-1], adler)
            print(adler, s[win:win+fullen], rolling_product(s[win:win+fullen]))
            for idx, x in enumerate(target_hashes):
                if adler == x:
                    if s[win:win+fullen] == target_strings[idx]:
                        solution.append(win)
                        break
        return solution

if __name__ == "__main__":
    S = Solution()
    print(S.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
    print(S.findSubstring(s = "wordgoodgoodgoodbestword",  words = ["word","good","best","word"]))
    # print(S.findSubstring(s = "barfoofoobarthefoobarman", words =["bar","foo","the"]))
    # print(S.findSubstring(s="wordgoodgoodgoodbestword", words=["word","good","best","good"]))

