
n, k = map(int, input().split()) 
a = list(map(int,input().split()))

hm = {}
for i in range(n):
    if a[i] in hm:
        hm[a[i]].append(i)
    else:
        hm[a[i]] = [i]            
a.sort()
i, ans = 0, []
while i < n and k > 0:
    k -= a[i]
    if k >= 0:

        ans.append(hm[a[i]][-1])
        hm[a[i]].pop()
    i += 1
print(len(ans))
for v in ans:
    print(v+1, end=" ")