n = int(input())
s = input()

count = [0,0] # H,T count
for v in s:
    if v == 'H':
        count[0] += 1
    else:
        count[1] += 1    
s = s+s
window = max(count[0], count[1])
wincount = [0,0]

for i in range(window):
    if s[i] == 'H':
        wincount[0] += 1
    else:
        wincount[1] += 1
ans = min(wincount[0], wincount[1])
left = 0

for i in range(window, 2*n):
    if s[i] == 'H':
        wincount[0] += 1
    else:
        wincount[1] += 1
    
    if s[left] == 'H':
        wincount[0] -= 1
    else:
        wincount[1] -= 1
    left += 1
        
    ans = min(ans, wincount[0], wincount[1])
print(ans)