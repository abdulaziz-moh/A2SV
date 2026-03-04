class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.queue:
            v = self.queue[0]
            for i in range(len(self.queue) - 1):
                self.queue[i] = self.queue[i+1]
            self.queue.pop()
            return v

    def peek(self) -> int:
        if self.queue:
            return self.queue[0]
        
    def empty(self) -> bool:
        if self.queue:
            return False
        return True
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()