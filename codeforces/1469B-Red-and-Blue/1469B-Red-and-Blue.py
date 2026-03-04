t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    
    mxa, mxb, prefix = 0, 0, 0
    for v in a:
        prefix += v
        mxa = max(mxa,prefix)
    prefix = 0
    for v in b:
        prefix += v
        mxb = max(mxb,prefix)
    print(mxa+mxb)