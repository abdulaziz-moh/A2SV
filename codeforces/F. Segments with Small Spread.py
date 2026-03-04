# import sys
# from collections import deque
# try:
#     line1 = sys.stdin.readline()
#     if not line1:
#         exit
#     n,s = map(int,line1.split())
    
#     line2 = sys.stdin.readline()
#     if not line2:
#         exit
#     a = list(map(int,line2.split()))
    
# except EOFError:
#     exit
# except ValueError:
#     exit

import sys
from collections import deque  
n,s = map(int,(sys.stdin.readline()).split())
a = list(map(int,(sys.stdin.readline()).split()))
l,ans = 0,0
max_deq = deque()
min_deq = deque()
for r in range(n):
    while max_deq and max_deq[-1] < a[r]:
        max_deq.pop()
    max_deq.append(a[r])
    while min_deq and min_deq[-1] > a[r]:
        min_deq.pop()
    min_deq.append(a[r])
    
    while max_deq[0] - min_deq[0] > s:
        if max_deq[0] == a[l]:
            max_deq.popleft()
        if min_deq[0] == a[l]:
            min_deq.popleft()
        l += 1
    ans += (r-l+1)
print(ans)