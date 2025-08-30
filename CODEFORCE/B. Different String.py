t = int(input())

for _ in range(t):
    r = input()
    s = r[0]
    length = len(r)
    for i in range(1, length):
        if s != r[i]:
            print("YES")
            print((r[i] + r[1:i] + s + r[i+1:]))
            break
    else:
        print("NO")