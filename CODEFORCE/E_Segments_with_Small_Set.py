from collections import defaultdict

n, s =map(int,input().split())
a = list(map(int,input().split()))

left, ans = 0, 0
unique = defaultdict(int)
for right in range(n):
    unique[a[right]] += 1
    while len(unique) > s:
        unique[a[left]] -= 1
        if unique[a[left]] == 0:
            del unique[a[left]]
        left += 1
    ans += (right - left + 1)
print(ans)