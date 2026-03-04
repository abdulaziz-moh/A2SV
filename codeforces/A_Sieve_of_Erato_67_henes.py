t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    for v in a:
        if v == 67:
            print('YES')
            break
    else:
        print('NO')