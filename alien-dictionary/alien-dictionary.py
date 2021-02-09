from collections import defaultdict

def findOrder(dictionary, N, K):
    def letterorder(fw, sw):
        l = min(len(fw), len(sw))
        for i in range(l):
            if fw[i] == sw[i]: continue
            return fw[i], sw[i]
        return None, None

    def toposort(v, topo, visited, stack):
        visited[v] = True
        if v in topo:
            for i in topo[v]:
                if not visited[i]:
                    toposort(i, topo, visited, stack)
        stack.append(v)
    
    topo = {}
    orders = [letterorder(dictionary[i], dictionary[i+1]) for i in range(len(dictionary)-1)]
    print(orders)
    for b, a in orders:
        if b in topo:
            topo[b].append(a)
        else:
            topo[b] = [a]
    print(topo)
    visited = defaultdict(bool)
    stack = []
    for k in topo:
        if not visited[k]:
            toposort(k, topo, visited, stack)
    print(stack)
    return "".join(stack[::-1])

print(findOrder(["baa", "abcd", "abca", "cab", "cad"], 5, 4))

