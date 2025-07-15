class Solution:
    def maxScoreIndices(self, nums):
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1 

        left = 0
        right = count
        ans = [0]
        max = count
        for i in range(1,n+1):

            if nums[i-1] == 0:
                left += 1
            else:
                right -= 1

            sum = left + right
            if sum > max:
                max = sum
                ans.clear()
                ans.append(i)
            elif sum == max:
                ans.append(i)

        return ans
nums = [0,0,1,0]
obj = Solution()
print(obj.maxScoreIndices(nums))
