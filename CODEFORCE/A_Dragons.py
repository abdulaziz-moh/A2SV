s,n = map(int,input().split())
a = []
for i in range(n):
    x = list(map(int,input().split()))
    a.append(x)
    j = i
    while j > 0:
        if a[j][0] < a[j-1][0]:
            a[j][0],a[j-1][0] = a[j-1][0],a[j][0]
            a[j][1],a[j-1][1] = a[j-1][1],a[j][1]
        else:
            break
        j -= 1
status = True
for v in a:
    if s > v[0]:
        s += v[1]
    else:
        status = False
        print("NO")
        break
if status:
    print("YES")