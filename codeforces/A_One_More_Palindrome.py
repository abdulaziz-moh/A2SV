from typing import Counter


t = int(input())
for _ in range(t):
    s = input()
    cnt = Counter(s)
    x = 2
    for v in cnt.values():
        if v >= 2:
            x -= 1
            if x <= 0:
                break
    if x <= 0:
        print('YES')
    else:
        print('NO')