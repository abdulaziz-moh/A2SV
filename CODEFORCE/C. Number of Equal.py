n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

l,r = 0,0
ans,sum = 0,0
while l < n and r < m:
    sum = 0
    if a[l] < b[r]:
        l += 1
    elif a[l] > b[r]:
        r += 1
    else:
        while l < n and b[r] == a[l]:
            sum += 1
            l += 1
        ans += sum
        r += 1
        while r < m and b[r] == b[r-1]:
            ans += sum
            r += 1
# while r < m and b[r] == b[r-1]:
#     ans += sum
#     r += 1
print(ans)
