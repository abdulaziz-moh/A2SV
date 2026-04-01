t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mx = a[-1]
    count = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            sum = a[i] + a[j]
            need = mx - sum
            if need < 0:
                count += (n-j-1)
                continue
            left, right = j + 1, n
            while left < n and left <= right:
                mid = (left + right )//2 
                if sum > a[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            end = right
            left = j + 1
            while left < n and left <= right:
                mid = (left + right )//2 
                if a[mid] > need:
                    right = mid - 1
                else:
                    left = mid + 1
            count += (end - right)
    print(count)
