t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    ans = 0
    count = 0
    for v in s:
        if v == '#':
            ans += count
            count = 0
        else:
            count += 1
            if count > 2:
                ans = 2
                count = 0
                break
    ans += count
    print(ans)