t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    n = sum(a)
    x = n%3
    if x == 0:
        print(n//3)
    elif x == 1:
        print(n//3 - 1)
    else:
        print((n+1)//3 + 1)
    # x = (3 - (n%3))%3
    # y = (n + x)//3
    # print(y+x)