def knapsack(values, weights, capacity):
    def knapsack_topdown(values, weights, capacity):
        def knapsack_recursive(values, weights, curcapacity, curindex, mem):
            if curcapacity <= 0 or curindex >= len(values): return 0
            if mem[curindex][curcapacity] is not None:
                return mem[curindex][curcapacity]
            p1 = 0
            if weights[curindex] <= curcapacity:
                p1 = values[curindex] + knapsack_recursive(values, weights,
                                                           curcapacity - weights[curindex],
                                                           curindex+1,
                                                           mem)
            p2 = knapsack_recursive(values, weights, curcapacity, curindex+1, mem)
            p  = max(p1, p2)
            mem[curindex][curcapacity] = p
            return p

        mem = [[None for _ in range(capacity+1)] for _ in range(len(values))]
        return knapsack_recursive(values, weights, capacity, 0, mem)

    def knapsack_bottomup(values, weights, capacity):
        mem = [[0 for _ in range(capacity+1)] for _ in range(len(values))]
        for i in range(len(values)):
            mem[i][0] = 0
        for c in range(1,capacity+1):
            mem[0][c] = values[0] if weights[0] <= c else 0
        for i in range(len(values)):
            for c in range(1,capacity+1):
                p1 = p2 = 0
                if weights[i] <= c:
                    p1 = values[i] + mem[i-1][c-weights[i]]
                p2 = mem[i-1][c]
                p = max(p1, p2)
                mem[i][c] = p
        return mem[len(values)-1][capacity]

    #return knapsack_topdown(values, weights, capacity)
    return knapsack_bottomup(values, weights, capacity)

print(knapsack([1,6,10,16], [1,2,3,5], 7))
print(knapsack([1,6,10,16], [1,2,3,5], 6))
