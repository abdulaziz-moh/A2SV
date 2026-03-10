class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        queue, ans = deque(), []

        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        ans.append(nums[queue[0]]) 

        for i in range(k, n):

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if queue[0] <= i-k:
                queue.popleft()
            ans.append(nums[queue[0]])
        return ans