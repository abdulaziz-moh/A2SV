t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    nc,zc = 0,0
    for v in a:
        if v == -1:
            nc += 1
        elif v == 0:
            zc += 1
    print((nc%2)*2 + zc)
            
