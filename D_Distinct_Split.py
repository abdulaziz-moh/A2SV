
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    prefix = [0]*n
    suffix = [0]*n
    a = set()
    a.add(s[0])
    prefix[0] = 1
    for i in range(1,n):
        if s[i] in a:
            prefix[i] = prefix[i-1]
        else:
            a.add(s[i])
            prefix[i] = prefix[i-1] + 1
    a = set()
    a.add(s[-1])
    suffix[-1] = 1
    for i in range(n-2,-1,-1):
        if s[i] in a:
            suffix[i] = suffix[i+1]
        else:
            a.add(s[i])
            suffix[i] = suffix[i+1] + 1
    mx = 0
    for i in range(n-1):
        mx = max(mx,prefix[i] + suffix[i+1])
        
    print(mx)