from collections import defaultdict
from typing import Counter
prt = defaultdict(int)
n = int(input())
p = []
for i in range(n-1):
    p.append(int(input()))
    prt[i+2] = p[-1]
    
# print(prt)    
count = Counter(p)
x = list(count.keys())
x.sort(reverse=True)
# print(x)
# print(count)
for v in x:
    if count[v] < 3:
        print('No')
        break
    count[prt[v]] -= 1
else:
    print('Yes')