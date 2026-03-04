n,k = map(int,input().split())
a = list(map(int,input().split()))

count = 0

for i in range(n):
    if a[i] > 0:
        if k:
           count += 1 
           k -= 1
        elif a[i] == a[i-1]:
            count += 1
        else:
            break
    else:
        break
print(count)