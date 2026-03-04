n,s = map(int,input().split())
a = list(map(int,input().split()))
l,c,sum,good = 0,0,0,0
for v in a:
    sum += v
    c += 1
    if sum > s:
        while sum > s:
            sum -= a[l]
            l += 1
            c -= 1
    good = max(c,good)
print(good)