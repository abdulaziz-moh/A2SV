n, s =map(int,input().split())
a = list(map(int,input().split()))

left, sum, min_seg = 0, 0, float('inf')
for right in range(n):
    sum += a[right]
    while sum >= s:
        min_seg = min(min_seg, right - left + 1)
        sum -= a[left]
        left += 1
if min_seg == float('inf'):
    print(-1)
else:
    print(min_seg)