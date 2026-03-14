
n, b = map(int,input().split())
a = list(map(int,input().split()))
arr, sum = [], 0
diff = []
for i in range(n):
    if a[i] % 2 == 0:
        arr.append(1)
    else:
        arr.append(-1)
    sum += arr[-1]
    if sum == 0 and i+1 < n:
        diff.append(abs(a[i+1] - a[i]))
count = 0
diff.sort()
for v in diff:
    if b - v >= 0:
        b -= v
        count += 1
    else:
        break
print(count)