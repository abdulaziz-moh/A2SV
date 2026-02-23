n = int(input())
a = list(map(int, input().split()))
sset = set()
for v in a:
    sset.add(v)
ans = 0
for i in range(1,n+1):
    if i not in sset:
        ans = i
print(ans)