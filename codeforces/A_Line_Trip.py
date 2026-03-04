t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    
    mx = a[0]
    for i in range(1,n):
        mx = max(mx,a[i]-a[i-1])
    mx = max(mx,2*(x-a[-1]))
    print(mx)