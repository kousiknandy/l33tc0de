from typing import List
from itertools import chain 

class Memo:
    def __init__(self):
        self.memo = dict()
        self.queue = []
        self.idx = 0

    def add_path(self, beginWord: str, path: List[str]):
        if beginWord not in self.memo:
            self.memo[beginWord] = [path]
            self.queue.append(beginWord)
        else:
            if len(path) == len(self.memo[beginWord][0]):
                self.memo[beginWord].append(path)
            if len(path) < len(self.memo[beginWord][0]):
                self.memo[beginWord] = [path]

    def get_path(self, word: str) -> List[str]:
        return self.memo.get(word)

    def __iter__(self):
        self.idx = 0
        return self
    
    def __next__(self):
        try:
            n = self.queue[self.idx]
            self.idx += 1
            return n
        except IndexError:
            raise StopIteration
        
    def __repr__(self):
        return self.memo.__repr__() + "\n" + self.idx.__repr__() + " " + self.queue.__repr__() 
    
class Solution:
    @classmethod
    def transformable(cls, wordFrom: str, wordTo: str) -> bool:
        dist = 0
        for i in range(len(wordFrom)):
            if wordFrom[i] != wordTo[i]:
                if dist:
                    return False
                dist = dist + 1
        return True if dist == 1 else False               
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        result = []
        m = Memo()
        m.add_path(endWord, [])
        if endWord not in wordList:
            return result
        for target in m:
            for w in wordList:
                if w == endWord:
                    continue
                if self.transformable(w, target):
                    p = m.get_path(target)
                    if p is not None:
                        for p2 in p:
                            p1 = [target]
                            p1.extend(p2)
                            #print(w, target, p1)
                            m.add_path(w, p1)
        print(m)
        target = beginWord
        in_dict = False
        for w in wordList:
            p = m.get_path(target)
            if not p:
                if self.transformable(w, target):
                    p = m.get_path(w)
            else:
                in_dict = True
            if not p:
                continue
            for p2 in p:
                p1 = [target, w] if not in_dict else [target]
                #print("    ", p, p1, p2)
                p1.extend(p2)
                if not result:
                    result.append(p1)
                else:
                    if len(p1) < len(result[0]):
                        result = [p1]
                    if len(p1) == len(result[0]):
                        result.append(p1)
            if in_dict:
                break
        return result
                    

S = Solution()
#print(S.transformable("abc", "abc"))
#print(S.transformable("abc", "axc"))
#print(S.transformable("abc", "xyz"))
print(S.findLadders("a", "c", ["a", "b", "c"]))
print(S.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(S.findLadders("hit", "cog", ["hot","cog","dot","dog","hit","lot","log"]))
print(S.findLadders("hit", "xyz", ["hot","dot","dog","lot","log","cog", "xyz"]))
print(S.findLadders("xyz", "cog", ["hot","dot","dog","lot","log","cog"]))
print(S.findLadders("hit", "cog", ["hot","dot","dog","lot","log"]))
