from collections import defaultdict, deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegrees = defaultdict(int)
        canbemade = defaultdict(int)
        ingredient = defaultdict(list)
        alreadymade = set()
        makequeue = deque(supplies)
        for prod, igrs in zip(recipes, ingredients):
            for i in igrs: 
                ingredient[i].append(prod)
                indegrees[prod] += 1
        result = [s for s in supplies if indegrees[s]]
        while len(makequeue):
            ig = makequeue.popleft()
            for r in ingredient[ig]:
                canbemade[r] += 1
                if canbemade[r] == indegrees[r]: 
                    result.append(r)
                    makequeue.append(r)
        return result
