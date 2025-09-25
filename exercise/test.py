
leftarr = [10,15,22,80]
rightarr = [5,8,11,15,60,90]
l,r = 0,0
# merged = []

n = len(leftarr)
m = len(rightarr)

# while l < n and r < m:
#     if leftarr[l] <= rightarr[r]:
#         merged.append(leftarr[l])
#         l += 1
#     else:
#         merged.append(rightarr[r])
#         r += 1
# merged.extend(leftarr[l:])
# merged.extend(rightarr[r:])
# print(merged)
sum = 0
max = 0
k = 3
for i in range(k):
    sum += rightarr[i]
    
for i in range(1,m-2):
    sum = sum - rightarr[i - 1] + rightarr[i + k-1 ]
    if sum > max:
        max = sum
print(max)