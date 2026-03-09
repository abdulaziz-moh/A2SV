class Solution:
    def minOperations(self, logs: List[str]) -> int:

        count = 0
        for v in logs:
            if v == "../":
                if count > 0:
                    count -= 1
            elif v != './':
                count += 1
        return count