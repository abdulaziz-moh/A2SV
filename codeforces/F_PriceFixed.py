n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))

a.sort(key = lambda a: a[1])
left, right, count, totalobj = 0, n-1, 0, 0

while left <= right:
    need = a[left][1] - totalobj
    if need <= 0:
        count += a[left][0]
        totalobj += a[left][0]
        left += 1
    
    elif a[right][0] >= need:
        a[right][0] -= need
        if a[right][0] == 0:
            right -= 1
        
        count += need * 2
        count += a[left][0]
        totalobj += (need + a[left][0])
        
        left += 1
    else:
        count += a[right][0] * 2
        totalobj += a[right][0]
        right -= 1
print(count)