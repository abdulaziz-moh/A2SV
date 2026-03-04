
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

i, ans = 0, []
for v in b:
    
    while i < n and a[i] < v:
        i += 1
    ans.append(i)
        
for v in ans:
    print(v, end=" ")