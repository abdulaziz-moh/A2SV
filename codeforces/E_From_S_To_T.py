q = int(input())

for _ in range(q):
    
    s = input()
    t = input()
    p = input()
    
    tcount = {}
    for v in t:
        if v in tcount:
            tcount[v] += 1
        else:
            tcount[v] = 1
    
    i,j = 0,0
    while i < len(s):
        while j < len(t) and t[j] != s[i]:
            j += 1
        if j == len(t):
            break
        tcount[t[j]] -= 1
        if tcount[t[j]] == 0:
            del tcount[t[j]]
        i += 1
        j += 1
    if i < len(s):
        print('NO')
        continue
    
    pcount = {}
    for v in p:
        if v in pcount:
            pcount[v] += 1
        else:
            pcount[v] = 1
    for key in tcount:
        if key not in pcount or pcount[key] < tcount[key]:
            print('NO')
            break
    else:
        print('YES')