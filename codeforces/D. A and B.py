import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    ia = []
    ib = []
    for i in range(n):
        if a[i] == 'a':
            ia.append(i)
        else:
            ib.append(i)         
    mai = math.ceil(len(ia)/2) - 1
    mbi = math.ceil(len(ib)/2) - 1
    sa,sb = 0,0
    for v in ia:
        sa += abs(v-ia[mai]) - 1
    for v in ib:
        sb += abs(v-ib[mbi]) - 1
    sa -= (math.floor(((len(ia)-2)/2)**2) - 1)
    sb -= (math.floor(((len(ib)-2)/2)**2) - 1)
    print(min(sa,sb))