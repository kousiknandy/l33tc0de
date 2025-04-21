class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = 0

    def next(self, price: int) -> int:
        self.day += 1
        while len(self.stack) > 0 and self.stack[-1][0] < price:
            self.stack.pop()
        if len(self.stack) == 0 or self.stack[-1][0] > price:
            self.stack.append((price, self.day))
        if self.stack[-1][0] == price:
            self.stack[-1] = (price, self.day)
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] > price:
                return self.day - self.stack[i][1]
        return self.day


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
