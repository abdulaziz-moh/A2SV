nums = [29,10,14,37,14]
n = len(nums)

for i in range(1,n):
    j = i -1
    while j > -1:
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1],nums[j]
            j -= 1
        else:
            break
print(nums)