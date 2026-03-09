class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        x = t - 3000
        while self.requests[0] < x:
            self.requests.popleft()
        return len(self.requests)