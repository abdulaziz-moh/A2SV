T = int(input())

for _ in range(T):
    s = input()
    t = input()
    
    hmt = {}
    for v in t:
        if v in hmt:
            hmt[v] += 1
        else:
            hmt[v] = 1
    status = True
    for v in s:
        if v in hmt and hmt[v] > 0:
            hmt[v] -= 1
        else:
            status = False
            print("Impossible")
            break
    if status:
        newsorted = sorted(hmt)
        sptr = 0
        nptr = 0
        ans = []
        while nptr < len(newsorted) and sptr < len(s) :
            
            if newsorted[nptr] < s[sptr]:
                for _ in range(hmt[newsorted[nptr]]):
                    ans.append(newsorted[nptr])
                nptr += 1
            elif newsorted[nptr] == s[sptr]:
                ans.append(s[sptr])
                sptr += 1
            else:
                ans.append(s[sptr])
                sptr += 1
        while nptr < len(newsorted):
            for _ in range(hmt[newsorted[nptr]]):
                ans.append(newsorted[nptr])
            nptr += 1
        while sptr < len(s):
            ans.append(s[sptr])
            sptr += 1
        print("".join(ans))
    
