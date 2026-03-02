n, s =map(int,input().split())
a = list(map(int,input().split()))

left, longest, sum = 0, 0, 0
for right in range(n):
    sum += a[right]
    while sum > s:
        sum -= a[left]
        left += 1
    longest = max(longest, right - left + 1)
print(longest)