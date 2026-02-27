from collections import Counter


n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

count = Counter(b)
ans = 0
for v in a:
    ans += count[v]
print(ans)