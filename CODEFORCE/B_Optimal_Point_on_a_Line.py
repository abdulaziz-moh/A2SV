n = int(input())
a = list(map(int,input().split()))

a.sort()
i = 0
if n%2 == 0:
    i = n//2 -1
else:
    i = n//2
print(a[i])