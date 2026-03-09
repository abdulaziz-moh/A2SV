class BrowserHistory:

    def __init__(self, homepage: str):
        self.backward_stack = [homepage]
        self.forward_stack = []

    def visit(self, url: str) -> None:
        self.backward_stack.append(url)
        self.forward_stack = []

    def back(self, steps: int) -> str:
        n = len(self.backward_stack)
        x = steps
        if steps >= n:
            x = n-1
        for _ in range(x):
            self.forward_stack.append(self.backward_stack.pop())
        return self.backward_stack[-1]

    def forward(self, steps: int) -> str:
        n = len(self.forward_stack)
        x = steps
        if steps > n:
            x = n
        for _ in range(x):
            self.backward_stack.append(self.forward_stack.pop())
        return self.backward_stack[-1]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)