from collections import Counter
q = int(input())
for _ in range(q):
    n = int(input())
    s,t = input().split()
    hms,hmt = Counter(),Counter()
    for i in range(n):
        hms[s[i]] += 1
        hmt[t[i]] += 1
    
    for v in hms:
        if hms[v] != hmt[v]:
            print("NO")
            break
    else:
        print("YES")