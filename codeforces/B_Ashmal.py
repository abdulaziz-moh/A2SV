t = int(input())
for _ in range(t):
    n = int(input())
    a = list(input().split())

    s = ""
    for v in a:
        if s+v < v+s:
            s = s + v
        else:
            s = v + s
    print(s)