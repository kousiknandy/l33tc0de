class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, src, dst, weight=1):
        self.add_node(src)
        self.add_node(dst)
        self.graph[src].append((dst, weight))

    def __str__(self):
        return str(self.graph)

    def bfs(self, src, uniq=True):
        q = [(x,1) for x in self.graph[src]]
        v = [x[0][0] for x in q]
        while len(q):
            #print("q: ", q)
            #print("v: ", v)
            i, d = q.pop(0)
            if i[0] not in v:
                v.append(i[0])
            for j in self.graph[i[0]]:
                if (j[0] not in v) or not uniq:
                    j = j[0], j[1] + i[1]
                    q.append((j, d+1))
            yield i, d

    def min_cost(self, src, dst):
        c = 65537
        for n, d in self.bfs(src, False):
            if n[0] == dst:
                if c > n[1]:
                    c = n[1]
        return c
            
if __name__ == "__main__":
    g = Graph()
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(2, 4, 3)
    g.add_edge(3, 5)
    g.add_edge(3, 6)
    g.add_edge(5, 4, 2)
    g.add_edge(6, 7)
    print(g)
    print()
    for n, d in g.bfs(2):
        print(n, d)
    print()
    for n, d in g.bfs(2, False):
        print(n, d)
    print()
    c = g.min_cost(2, 4)
    print(c)
    print()

