t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    for i in range(n-3):
        if s[i:i+2] in s[i+2:]:
            print('YES')
            break
    else:
        print('NO')
        
        # sset = set()
    # status = False
    # for i in range(0,n,2):
    #     x = s[i:i+2]
        
    #     if x in sset:
    #         print('YES')
    #         status = True
    #         break
    #     sset.add(x)
    # sset = set()
    # if status:
    #     continue
    # for i in range(1,n,2):
    #     x = s[i:i+2]
        
    #     if x in sset:
    #         print('YES')
    #         status = True
    #         break
    #     sset.add(x)
    # if not status:
    #     print('NO')
