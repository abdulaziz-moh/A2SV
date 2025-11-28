from collections import Counter, deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        count = Counter(students)
        i = 0
        while queue:
            v = queue.popleft()
            if v == sandwiches[i]:
                i += 1
                count[v] -= 1
            else:
                queue.append(v)
                if count[v] == len(queue):
                    return count[v]
        return 0