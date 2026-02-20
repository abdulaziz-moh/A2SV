
n, k = map(int, input().split())
a = list(map(int, input().split()))

gap = []
for i in range(1,n):
    gap.append(a[i]-a[i-1])
gap.sort(reverse=True)
ans = 0
for i in range(k-1,n-1):
    ans += gap[i]
print(ans)
    