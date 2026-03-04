t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    mx = 0
    for i in range(0,n-1,2):
        s = a[i] - a[i+1]
        if s < 0:
            s *= -1
        if s > mx:
            mx = s
    print(mx)