import sys
input = sys.stdin.read
data = input().split()
t = int(data[0])
for _ in range(t):
    a = int(data.split())
    # a = list(map(int,input().split()))
    # print(a)
    if a[0] == a[1] == a[2] == a[3]:
        print("YES")
    else:
        print("NO")