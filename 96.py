class StockSpanner:

    # stack to store all the elements that are coming

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        currspan = 1

        while self.stack and self.stack[-1][0] <= price:
            currspan += self.stack.pop()[1]

        self.stack.append((price, currspan))
        return currspan

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)