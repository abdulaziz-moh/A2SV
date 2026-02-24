n,m = map(int, input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

l,r = 0,0
ans = []
s1,s2 = len(arr1),len(arr2)
while l < s1 and r < s2:
    if arr1[l] < arr2[r]:
        ans.append(arr1[l])
        l += 1
    elif arr1[l] == arr2[r]:
        ans.append(arr1[l])
        ans.append(arr1[l])
        l += 1
        r += 1
    else:
        ans.append(arr2[r])
        r += 1
ans.extend(arr1[l:])
ans.extend(arr2[r:])
for v in ans:
    print(v, end=" ")