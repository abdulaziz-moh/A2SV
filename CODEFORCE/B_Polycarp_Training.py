n = int(input())
a = list(map(int,input().split()))
a.sort()
c = 1
for v in a:
    if v >= c:
        c += 1
print(c-1)