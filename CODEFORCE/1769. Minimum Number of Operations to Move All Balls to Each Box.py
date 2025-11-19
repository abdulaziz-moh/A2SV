class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0]*n

        # left sum
        moves = 0
        balls = 0
        for i in range(n):
            ans[i] += moves
            if boxes[i] == '1':
                balls += 1
            moves += balls
        # right sum
        moves = 0
        balls = 0
        for i in range(n-1,-1,-1):
            ans[i] += moves
            if boxes[i] == '1':
                balls += 1
            moves += balls
        return ans