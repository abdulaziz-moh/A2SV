
from typing import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    count = Counter(a)
    if len(count) > 2:
        print("No")
    elif len(count) == 1:
        print('Yes')
    else:
        i = 1
        sum = 0
        for cnt in count.values():
            sum += ((cnt)*i)
            i = -1
        if abs(sum) > 1:
            print('No')
        else:
            print('Yes')