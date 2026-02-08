t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    l = 0
    r = 3
    status = False
    while r < n:
        c = s[l:r+1]
        if c == "2026":
            status = False
            
            break
        elif c == "2025":
            status = True
        l += 1
        r += 1
    
    if status:
        print('1')
    else:
        print('0')
