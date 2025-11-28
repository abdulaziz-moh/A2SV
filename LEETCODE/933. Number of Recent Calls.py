from collections import deque


class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        mn = t - 3000
        while self.requests[0] < mn:
            self.requests.popleft()
        return len(self.requests)