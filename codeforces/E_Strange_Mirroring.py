import sys, math, string
sys.setrecursionlimit(10**7)


def rec(idx, parentstatus):
    if idx < 4:
        x = idx % 4
        if parentstatus[0] == False:
            if x == 0 or x == 3:
                parentstatus[0]  = False
            else:
                parentstatus[0]  = True
        else:
            if x == 0 or x == 3:
                parentstatus[0]  = True
            else:
                parentstatus[0]  = False
        return
    
    a = math.ceil(math.log(idx) / math.log(4))

    temp = 4 ** (a-1)
    mypos = ((idx) // (temp) )
    
    newidx = idx - (temp * mypos)
    if parentstatus[0] == False:
        if mypos == 0 or mypos == 3:
            parentstatus[0]  = False
        else:
            parentstatus[0]  = True
    else:
        if mypos == 0 or mypos == 3:
            parentstatus[0]  = True
        else:
            parentstatus[0]  = False
    return rec(newidx, parentstatus)

hm = {c: c.swapcase() for c in string.ascii_letters}

t = int(input())
for _ in range(t):
    s = input()
    q = int(input())
    k = list(map(int, input().split()))
    
    submit = []
    n = len(s)
    
    for v in k:
        idx = (v-1)//n
        ans = [True]
        rec(idx, ans)
        
        newidx = (v - 1) % n
        if ans[0]:
            submit.append(s[newidx])
        else:
            submit.append(hm[s[newidx]])
    print(*submit)