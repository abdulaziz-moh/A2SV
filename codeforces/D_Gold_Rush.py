t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
        
    stack = [n]
    while stack:
        if stack[-1] == m:
            print('YES')
            break
        if stack[-1] % 3 == 0:
            x = stack[-1] // 3
            y = 2*x
            stack.pop()
            stack.append(x)
            stack.append(y)
        else:
            stack.pop()
    else:
        print('NO')