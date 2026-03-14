t = int(input())
for _ in range(t):
    n = int(input())
    num = input()
    
    a = []
    c = 2
    for v in num:
        if int(v) % 2 != 0:
            a.append(v)
            c -= 1
        if c <= 0:
            break
    if len(a) < 2:
        print(-1)
    else:
        print("".join(a))
    
    # a = []
    # for v in num:
    #     a.append(int(v))
        
    # x = -1
    # for i in range(n-1,-1,-1):
    #     if a[i] % 2!= 0:
    #         if x == -1:
    #             x = i
    #         else:
    #             x = -1
    # if x != -1:
    #     for i in range(x,n-1):
    #         a[i] = a[i+1]
    #     a.pop()
        
    # for i in range(len(a)-1,-1,-1):
    #     if a[i] % 2 == 0:
    #         a.pop()
    #     else:
    #         break
    # if not a:
    #     print(-1)
    # else:
    #     print("".join(map(str,a)))