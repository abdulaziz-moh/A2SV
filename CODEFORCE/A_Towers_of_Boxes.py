import math
t = int(input())
for _ in range(t):
    n,m,d = map(int,input().split())
    if m > d:
        print(n)
    else:
        print(math.ceil(n/((d//m) + 1)))