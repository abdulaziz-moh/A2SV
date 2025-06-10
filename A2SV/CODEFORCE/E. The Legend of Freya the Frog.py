import math
t = int(input())
for i in range(t):
    x,y,k = map(int,input().split())
    maximum = max(x,y)
    count = 0
    if x >= y+k:
        count = (2 * math.ceil(maximum/k)) - 1
    else:
        count = (2 * math.ceil(maximum/k))
    print (count)