nums=[1,2,1,3,3,4,6,8,4,2,6,8,4]
l = max(nums) + 1
aux_arr = [0] * l
for v in nums:
    aux_arr[v] += 1
x = 0
for i in range(l):
    for _ in range(aux_arr[i]):  
        nums[x] = i
        x += 1
print(nums)

# to make it generally work for negative numbers also

nums=[1,2,-1,-3,-3,4,6,8,4,-2,6,8,-4]
maximum = max(nums)
minimum = abs(min(nums))
l = maximum + minimum + 1
count = [0] * l

for v in nums:
    count[v+minimum] += 1

x = 0
for i in range(l):
    for _ in range(count[i]):
        nums[x] = i - minimum
        x +=1
print(nums)