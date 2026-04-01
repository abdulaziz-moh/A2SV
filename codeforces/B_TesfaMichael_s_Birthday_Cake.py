n, k = map(int, input().split())
s = input()
length = [ord(ch) - ord('a') + 1 for ch in s]
length.sort()

temp = length[0]
sum = temp
count = 1
if count == k:
    print(sum)
    exit()
for i in range(1,n):
    if length[i] >= temp+2:
        sum += length[i]
        count += 1
        temp = length[i]
    if count == k:
        print(sum)
        break
else:
    print(-1)