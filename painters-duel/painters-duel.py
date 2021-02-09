import copy

class museum():
    EMPTY, ALMA, BERTHE, CONSTR = 0, 1, 2, 3
    
    def __init__(self, size):
        self.rooms = [self.EMPTY] * (size * size)
        self.size  = size
        self.alma  = None
        self.berthe = None

    def next_room(self, p):
        pa, pb = p
        if pb > 1:
            yield (pa, pb - 1)
        if pb < (2 * self.size - 1):
            yield (pa, pb + 1)
        if pb % 2:
            if pa < self.size and pb < (2 * self.size - 1):
                yield (pa + 1, pb + 1)
        else:
            if pa > 1 and pb > 1:
                yield (pa - 1, pb - 1)

    def next_move(self, p):
        moves = []
        for m in self.next_room(p):
            if self.rooms[self._room(m)] == self.EMPTY:
                moves.append(m)
        return moves

            
    def __deepcopy__(self, memo):
        c = museum(self.size)
        c.alma = self.alma
        c.berthe = self.berthe
        c.rooms = copy.deepcopy(self.rooms)
        return c

    def __repr__(self):
        s = str(self.size) + ": "
        for i, r in enumerate(self.rooms):
            if r == self.EMPTY: s += "E"
            elif r == self.ALMA: s += "A"
            elif r == self.BERTHE: s += "B"
            else: s += "C"
            if self.alma and i == self._room(self.alma): s += "*"
            if self.berthe and i == self._room(self.berthe): s += "*"
        return s

    def _room(self, r):
        return (r[0] - 1) ** 2 + (r[1] - 1)
    
    def paint(self, r, person):
        self.rooms[self._room(r)] = person

    def construction(self, r):
        self.paint(r, self.CONSTR)

    def score(self):
        a = 0
        b = 0
        for r in self.rooms:
            if r == self.ALMA: a += 1
            if r == self.BERTHE: b += 1
        return a - b
    
def best_score(game_pos, player_turn, depth = 0):
    #print(" " * depth, game_pos, player_turn)
    next_games = []
    for move in game_pos.next_move(game_pos.alma if player_turn == museum.ALMA else game_pos.berthe):
        game = copy.deepcopy(game_pos)
        game.paint(move, player_turn)
        if player_turn == museum.ALMA:
            game.alma = move
        else:
            game.berthe = move
        next_games.append(game)
    if not next_games:
        if not game_pos.next_move(game_pos.alma if player_turn == museum.BERTHE else game_pos.berthe):
            return game_pos.score()
        else:
            game = copy.deepcopy(game_pos)
            next_games.append(game)
    scores = map(lambda g: best_score(g,
                                      museum.ALMA if player_turn == museum.BERTHE else museum.BERTHE,
                                      depth+1),
                 next_games)
    if player_turn == museum.ALMA:
        return max(scores)
    else:
        return min(scores)
    

T = int(input())
for tc in range(1, T+1):
    s, a0, a1, b0, b1, c = map(int, input().split())
    m = museum(s)
    m.alma = (a0, a1)
    m.paint((a0, a1), museum.ALMA)
    m.berthe = (b0, b1)
    m.paint((b0, b1), museum.BERTHE)
    for _ in range(c):
        c0, c1 = map(int, input().split())
        m.construction((c0, c1))
    s = best_score(m, museum.ALMA)
    print("Case #{}: {}".format(tc, s))


exit()

m = museum(3)
m.alma = (3,1)
m.paint((3,1), museum.ALMA)
m.berthe = (2,3)
m.paint((2,3), museum.BERTHE)
s = best_score(m, museum.ALMA)
print(s)

m = museum(2)
m.alma = (1,1)
m.paint((1,1), museum.ALMA)
m.berthe = (2,1)
m.paint((2,1), museum.BERTHE)
s = best_score(m, museum.ALMA)
print(s)

m = museum(2)
m.alma = (2,2)
m.paint((2,2), museum.ALMA)
m.berthe = (1,1)
m.paint((1,1), museum.BERTHE)
m.construction((2,1))
m.construction((2,3))
s = best_score(m, museum.ALMA)
print(s)

m = museum(3)
m.alma = (3,4)
m.paint((3,4), museum.ALMA)
m.berthe = (2,1)
m.paint((2,1), museum.BERTHE)
m.construction((3,1))
m.construction((2,3))
s = best_score(m, museum.ALMA)
print(s)

m = museum(3)
m.alma = (3,2)
m.paint((3,2), museum.ALMA)
m.berthe = (2,3)
m.paint((2,3), museum.BERTHE)
m.construction((2,1))
m.construction((3,1))
s = best_score(m, museum.ALMA)
print(s)
