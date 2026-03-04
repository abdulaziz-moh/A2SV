t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    if min(a) == a[0]:
        print('YES')
    else:
        print('NO')