m,n = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
merged = []
ap, bp = 0, 0
while ap < m and bp < n:
    if a[ap] <= b[bp]:
        print(a[ap], end = " ")
        # merged.append(a[ap])
        ap += 1
    else:
        print(b[bp], end = " ")
        # merged.append(b[bp])
        bp += 1
while ap < m:
    print(a[ap], end = " ")
    # merged.append(a[ap])
    ap += 1
while bp < n:
    print(b[bp], end = " ")
    # merged.append(b[bp])
    bp += 1
# for val in merged:
#     print(val, end =" ")