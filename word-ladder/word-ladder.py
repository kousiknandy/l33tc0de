from typing import List
import string
from collections import deque

class Solution:
    def nextword(self, word, wordict):
        for i,c in enumerate(word):
            for x in string.ascii_lowercase:
                if x == c: continue
                neww = word[:i] + x + word[i+1:]
                if neww in wordict:
                    yield neww
                    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        worDict = {x: 0 for x in wordList}
        if endWord not in worDict: return 0
        procque = deque()
        procque.append((beginWord,0))
        worDict[beginWord] = 1
        while len(procque) > 0:
            word, step = procque.popleft()
            print(word, step)
            if word == endWord:
                return step
            worDict[word] = 1
            for nextw in self.nextword(word, worDict):
                if worDict[nextw] == 1:
                    continue
                worDict[nextw] = 1
                procque.append((nextw, step+1))
        return 0

S = Solution()
print(S.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))   
