t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    i = 1
    if a[0] != 1:
        print("NO")
        continue
    
    
    
    while i < n-1:
        if a[i] == i+1:
            i += 1
            continue
        elif i+1 == a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            i += 1
            continue
        print("NO")
        break
    else:
        print("YES")
    print(a)
            