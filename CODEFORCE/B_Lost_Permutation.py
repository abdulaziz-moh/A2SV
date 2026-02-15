t = int(input())
for _ in range(t):
    m,s = map(int, input().split())
    b = list(map(int,input().split()))
    
    mn = min(b)
    if len(set(b)) != len(b) or mn <= 0:
        print('NO')
        continue
    b.sort()
    mx = b[-1]
    idx,rem = 0,0
    for i in range(1,mx):
        if b[idx] == i:
            idx += 1
            continue
        rem += i
    s -= rem
    rem = s
    mx += 1
    while rem >= mx:
        rem -= mx
        if rem == 0:
            break
        mx += 1

    if rem != 0:
        print('NO')
    else:
        print('YES')
