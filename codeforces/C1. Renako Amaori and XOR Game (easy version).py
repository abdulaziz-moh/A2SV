t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ca,cb = 0,0
    sa,sb = True,True
    
    for i in range(n):
        if a[i] == 1:
            ca += 1

    if ca%2 == 0:
        sa = False
        for i in range(0,n,2):
            if a[i] != b[i]:
                a[i] = 1
                b[i] = 0
                sa = True
                break
    for i in range(n):
        if b[i] == 1:
            cb += 1
    if cb%2 == 0:
        sb = False
        for i in range(1,n,2):
            if b[i] != a[i]:
                sb = True
                a[i] = 0
                b[i] = 1
                break
    if sa and sb:
        print("Tie")
    elif sa:
        print("Ajisai")
    elif sb:
        print("Mai")