t = int(input())
for _ in range(t):
    s = input()
    i,n = 0, len(s)
    res = set()
    while i < n:
        if i + 1 >= n:
            res.add(s[i])
        elif s[i] != s[i+1]:
            res.add(s[i])
        else:
            i += 1
        i += 1
    ans = sorted(list(res)) 
    print("".join(ans))