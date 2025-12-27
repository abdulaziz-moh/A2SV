t = int(input())
for _ in range(t):
    s = input()
    c = 0
    for v in s:
        if v == "Y":
            c += 1
            if c > 1:
                print('NO')
                break
    else:
        print("YES")