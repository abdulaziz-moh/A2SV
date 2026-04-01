a, b = map(int, input().split())
ans = [b]
while b >= a:
    if b == a:
        print('YES')
        print(len(ans))
        ans.reverse()
        print(*ans)
        break
    if b % 2 == 0:
        b //= 2
        ans.append(b)
    elif (b-1) % 10 == 0:
        b -= 1
        b //= 10
        ans.append(b)
    else:
        b = a-1
        
else:
    print('NO')