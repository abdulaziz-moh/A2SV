from typing import Counter


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    count = Counter(a)
    ans = 0
    for num in count.values():
        ans += (num//3)
    print(ans)