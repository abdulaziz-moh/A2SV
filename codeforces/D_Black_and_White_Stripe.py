for _ in range(int(input())):
    n, k = map(int,input().split())
    s = input()
    count, left = 0, 0
    for i in range(k):
        if s[i] == 'W':
            count += 1
    ans = count
    for right in range(k,n):
        if s[right] == 'W':
            count += 1
        if s[left] == 'W':
            count -= 1
        left += 1
        ans = min(ans, count)
    print(ans)