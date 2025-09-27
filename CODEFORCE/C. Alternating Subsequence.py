t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    mx,i,ans = 0,0,0
    while i <n:
        if a[i] >0:
            mx = 0
            while i<n and a[i] >0:
                mx = max(mx,a[i]) 
                i += 1  
        else:
            mx = a[i]
            while i<n and a[i] <0:
                mx = max(mx,a[i])
                i += 1
        ans += mx
    print(ans)