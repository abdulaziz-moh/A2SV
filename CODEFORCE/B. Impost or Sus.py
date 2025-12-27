t = int(input())
for _ in range(t):
    r = input()
    i,c = 1,0
    l = len(r)
    ch = -1
    while i < l-1:
        if r[i] == 'u':
            if r[i+1] == 'u':
                c += 1
                i += 1
                ch = i
        i += 1
    if r[0] == 'u':
        c += 1
    if r[l-1] == 'u' and (r[l-2] == 's' or ch == l-2):
        c += 1
    print(c)
