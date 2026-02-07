t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    set1 = set()
    
    prefix = [0]*n
    suffix = [0]*n
    prefix[0] = 1
    set1.add(s[0])
    suffix[-1] = 1
    for i in range(1,n):
        if s[i] in set1:
            prefix[i] = prefix[i-1]
        else:
            prefix[i] = prefix[i-1] + 1
            set1.add(s[i])
            
    set1.clear()
    set1.add(s[-1])
    for i in range(n-2,-1,-1):
        if s[i] in set1:
            suffix[i] = suffix[i+1]
        else:
            suffix[i] = suffix[i+1] + 1
            set1.add(s[i])
    mx = 0

    for i in range(n-1):
        mx = max(mx,prefix[i]+suffix[i+1])
    print(mx)