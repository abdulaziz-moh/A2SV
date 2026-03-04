t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    mxi,mxv = 0, 0
    
    for i,x in enumerate(a):
        if x > mxv:
            mxv = x
            mxi = i
            
    if a[0] == mxv or a[n-1] == mxv:
        print("NO")
        continue
    status = True
    while True:
        for i,x in enumerate(a):
            if x > mxv:
                mxv = x
                mxi = i
        if mxv == 0:
            print("YES")
            break
        if a[0] == mxv or a[n-1] == mxv:
            print("NO")
            status = False
            print(mxi,": ",mxv)
            break

        a[mxi] -= 2
        a[mxi-1] -= 1
        a[mxi+1] -= 1
        
        if a[mxi] < 0 or a[mxi-1] < 0 or a[mxi+1] < 0:
            print("NO")
            status = False
            break
        mxv -= 2

        