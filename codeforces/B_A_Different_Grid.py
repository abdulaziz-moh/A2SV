t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp)
    if not arr or len(arr) <= 1 and len(arr[0]) <= 1:
        print(-1)
        continue 
     
    for i in range(n):
        for j in range(m-1):
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
    for i in range(m):
        for j in range(n - 1):
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
    for v in arr:
        print(*v)