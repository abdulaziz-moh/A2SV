n,k = map(int,input().split())
a = input()

i = 0
while i < n:
    count = 0
    if a[i] == '.':
        i += 1
        continue
    while i < n and a[i] == '#':
        count += 1
        i += 1
    if count >= k:
        print('NO')
        break
else:
    print('YES')