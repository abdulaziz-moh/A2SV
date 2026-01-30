t = int(input())
for _ in range(t):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if k != 1:
        print("YES")
    else:
        if a == sorted(a):
            print("YES")
        else:
            print("NO")