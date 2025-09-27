nums = [29,10,14,37,14]
n = len(nums)

for i in range(1,n):
    for j in range(n-i):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
print(nums)