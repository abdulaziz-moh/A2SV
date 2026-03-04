n,s = map(int,input().split())
a = list(map(int,input().split()))
l,c,sum,ans = 0,0,0,float("inf")
for v in a:
    sum += v
    c += 1
    if sum >= s:
        while sum >= s:
            ans = min(ans,c)
            sum -= a[l]
            l += 1
            c -= 1
            
if ans == float("inf"):
    print(-1)
else:  
    print(ans)