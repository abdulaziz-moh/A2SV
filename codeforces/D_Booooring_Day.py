t = int(input())
for _ in range(t):
    n, l,r = map(int,input().split())
    a = list(map(int,input().split()))
    
    count, sum, left = 0, 0, 0
    
    for right in range(n):
        sum += a[right]
        while left <= right and sum > r:
            sum -= a[left]
            left += 1
        if l <= sum <= r:
            count += 1
            sum = 0
            left = right + 1 
    print(count)
