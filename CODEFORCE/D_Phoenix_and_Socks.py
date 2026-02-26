t = int(input())
for _ in range(t):
    n, l, r = map(int,input().split())
    c = list(map(int,input().split()))
    
    lhm = {}
    for i in range(l):
        if c[i] in lhm:
            lhm[c[i]] += 1
        else:
            lhm[c[i]] = 1
    rhm = {}
    for i in range(l,n):
        if c[i] in rhm:
            rhm[c[i]] += 1
        else:
            rhm[c[i]] = 1

    for i in range(l):
        if c[i] in rhm:
            lhm[c[i]] -= 1
            rhm[c[i]] -= 1
            if lhm[c[i]] == 0:
                del lhm[c[i]]
            if rhm[c[i]] == 0:
                del rhm[c[i]]
    lcount, rcount = 0,0
    la, ra = 0,0
    for v in lhm.values():
        lcount += v
        la += (v//2)
        
    for v in rhm.values():
        rcount += v
        ra += (v//2)
        
    if lcount == rcount:
        print(lcount)
        continue

    else:
        ans = 0
        if rcount > lcount:
            ans += lcount
            rcount -= lcount
            while ra > 0 and rcount >= 2:
                ans += 1
                rcount -= 2
                ra -= 1
            ans += rcount                

        else:
            ans += rcount
            lcount -= rcount
            while la > 0 and lcount >= 2:
                ans += 1
                lcount -= 2
                la -= 1
            ans += lcount

    print(ans)