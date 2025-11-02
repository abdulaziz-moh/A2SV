n,s = map(int,input().split())
a = list(map(int,input().split()))
l,ans = 0,0
freq = {}
for r in range(n):
    if a[r] in freq:
        freq[a[r]] += 1
    else:
        freq[a[r]] = 1
        
    while len(freq) > s:
        freq[a[l]] -= 1
        if freq[a[l]] == 0:
            del freq[a[l]]
        l += 1
    ans += (r-l+1)
print(ans)