t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    arr = []
    for _ in range(k):
        temp = list(map(int, input().split()))
        arr.append(temp)
        
    arr.sort()
    # print(arr)
    newarr = []
    i = 0
    while i < k:
        brand = arr[i][0]
        newarr.append(0)
        while i < k and arr[i][0] == brand:
            newarr[-1] += arr[i][1]
            i += 1
    
    newarr.sort(reverse=True)
    # print(newarr)
    ans = 0
    x = min(n,k,len(newarr))
    for i in range(x):
        ans += newarr[i]
    print(ans)