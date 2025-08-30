t = int(input())
for _ in range(t):
    a = input()
    count = 0
    for c in a:
        if c == 'N':
            count += 1
            if count > 1:
                print('YES')
                break  
    if count == 0:
        print('YES')
    elif count == 1:
        print('NO')    