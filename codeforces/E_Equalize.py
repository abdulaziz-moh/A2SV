t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    a.append(float("inf"))
    arr = []
    for i in range(n):
        if a[i] != a[i-1]:
            arr.append(a[i])
        
    r = 0
    mx = 0
    arrl = len(arr)
    for l in range(arrl):
        temp = arr[l] + n
        while r < arrl and arr[r] < temp:
            r += 1
        mx = max(mx, r-l)
    print(mx)