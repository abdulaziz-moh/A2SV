from collections import defaultdict

n, k = map(int,input().split())
a = list(map(int,input().split()))

ans, mx, left = [0,0], 0, 0
hm = defaultdict(int)
for right in range(n):
    hm[a[right]] += 1
    while len(hm) > k:
        hm[a[left]] -= 1
        if hm[a[left]] == 0:
            del hm[a[left]]
        left += 1
    window = right - left + 1
    if window > mx:
        mx = window
        ans = [left+1,right+1]
print(ans[0],ans[1])