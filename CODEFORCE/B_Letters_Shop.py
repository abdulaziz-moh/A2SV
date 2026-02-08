from typing import Counter


n = int(input())
s = input()
m = int(input())
sc = {}
for i in range(n):
    if s[i] in sc:
        sc[s[i]].append(i)
    else:
        sc[s[i]] = [i]

for _ in range(m):
    t = input()
    tc = Counter(t)
    mx = 0
    
    for key,value in tc.items():
        x = sc[key][value-1]
        mx = max(mx,x)
  
    print(mx+1)
