t = int(input())
for _ in range(t):
    n,x,k = map(int,input().split())
    s = input()
    
    i = 0
    while k > 0 and i < n:
        
        x += (-1 if s[i] == 'L' else 1)
        k -= 1
        i += 1
        if x == 0:
            break
        
    else:
        print('0')
        continue
    
    i = 0
    x = 0
    kbefore = k
    while k > 0 and i < n:
        x += (-1 if s[i] == 'L' else 1)
        k -= 1
        i += 1
        if x == 0:
            break
        
    else:
        print('1')
        continue
    print((kbefore//(i)) + 1)
            
    