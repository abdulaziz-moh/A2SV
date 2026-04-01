from collections import deque


n, k = map(int, input().split())
h = list(map(int, input().split()))

inc, dec = deque(), deque()
mx = -1
ans = []
left = 0

for right in range(n):
    while inc and h[right] <= h[inc[-1]]:
        inc.pop()
    inc.append(right)
    
    while dec and h[right] >= h[dec[-1]]:
        dec.pop()
    dec.append(right)
    
    while h[dec[0]] - h[inc[0]] > k:
        left += 1
        if dec[0] < left:
            dec.popleft()
        if inc[0] < left:
            inc.popleft()
    
    width = right - left + 1
    if width > mx:
        ans = []
        mx = width
        ans.append([left+1, right+1])
    elif width == mx:
        ans.append([left+1, right+1])
        
print(mx, len(ans))
for v in ans:
    print(*v)