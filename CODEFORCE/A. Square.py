t = int(input())
for _ in range(t):
    a = list(map(int,input().split()))
    if a[0] == a[1] == a[2] == a[3]:
        print("YES")
    else:
        print("NO")