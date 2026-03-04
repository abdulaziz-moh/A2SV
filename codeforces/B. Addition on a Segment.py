t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int,input().split()))
    c,x = 0,n

    for v in b:
        if v != 0:
            c += 1
            x = x - v + 1
    if x < 1:
        print(c)
    else:
        print(c - x + 1)