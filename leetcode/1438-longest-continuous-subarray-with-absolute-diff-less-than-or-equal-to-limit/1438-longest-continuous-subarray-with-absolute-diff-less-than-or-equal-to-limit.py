class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dec_queue, inc_queue = deque(), deque()
        ans, n, left = 0, len(nums), 0

        for i in range(n):
            x = nums[i]
            while dec_queue and nums[dec_queue[-1]] < x:
                dec_queue.pop()
            dec_queue.append(i)
            while inc_queue and nums[inc_queue[-1]] > x:
                inc_queue.pop()
            inc_queue.append(i)
            
            while abs(nums[inc_queue[0]] - nums[dec_queue[0]]) > limit:
                if inc_queue[0] < dec_queue[0]:
                    left = inc_queue[0] + 1
                    inc_queue.popleft()
                else:
                    left = dec_queue[0] + 1
                    dec_queue.popleft()

            ans = max(ans, i - left + 1)
            # print(inc_queue)
            # print(dec_queue)
            # print(ans)
            # print("----------------")
        return ans