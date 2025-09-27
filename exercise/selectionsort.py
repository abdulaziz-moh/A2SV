nums = [29,10,14,37,14]
n = len(nums)

for i in range(n-1):
    insert_position, min_index = i,i
    for j in range(i+1,n):
        if nums[j] < nums[min_index]:
            min_index = j
    nums[i],nums[min_index] = nums[min_index],nums[i]
print(nums)