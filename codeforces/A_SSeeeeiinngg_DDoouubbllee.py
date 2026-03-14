t = int(input())
for _ in range(t):
    s = input()
    a = []
    for i in range(len(s)-1,-1,-1):
        a.append(s[i])
    x = "".join(a) + s
    print(x)
    