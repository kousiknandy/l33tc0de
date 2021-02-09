lvl = 3
memo = True

class Solution:
    dp = {}
    def hashlist(self, choices):
        return tuple(sorted(choices))
    
    def playtree(self, player, remtotal, remchoices, depth = 0):
        #print(" "*depth, remchoices, remtotal)
        if memo:
            res = self.dp.get((remtotal, player, self.hashlist(remchoices)))
            if res is not None:
                print(" "*depth, "dp hit", (remtotal, player, self.hashlist(remchoices)), res)
                return res
        for c in remchoices:
            if c >= remtotal:
                self.dp[(remtotal, player, self.hashlist(remchoices))] = player == 0
                return player == 0 
        for c in remchoices:
            choices = [x for x in remchoices if x != c]
            res = self.playtree(1 if player == 0 else 0,
                                remtotal - c,
                                choices,
                                depth + 1)
            if player == 1:
                if res == False:
                    if depth < lvl: print(" "*depth, "calculated", (remtotal, player, self.hashlist(remchoices)), res)
                    self.dp[(remtotal, player, self.hashlist(remchoices))] = res
                    return False
            if player == 0:
                if res == True:
                    if depth < lvl: print(" "*depth, "calculated", (remtotal, player, self.hashlist(remchoices)), res)
                    self.dp[(remtotal, player, self.hashlist(remchoices))] = res
                    return True
        #print(" "*depth, results)
        self.dp[(remtotal, player, self.hashlist(remchoices))] = player == 1
        if depth < lvl: print(" "*depth, "calculated", (remtotal, player, self.hashlist(remchoices)), player == 1)
        return player == 1
        
    
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        return self.playtree(0, desiredTotal, list(range(maxChoosableInteger, 0, -1)))

S = Solution()
# print(S.canIWin(10, 15))
# print(S.canIWin(10, 11))
# print(S.canIWin(10, 25))
# print(S.canIWin(18, 79))
# print(S.canIWin(20, 210))
print(S.canIWin(18, 188))

#print(S.playtree(0, 22, [3, 4, 6, 7, 8, 9]))
