import sys
input_v = sys.stdin.read().split()

t = int(input_v[0])
ptr = 1

for _ in range(t):
    s = input_v[ptr]
    ptr += 1
    
    hm = {'R':'r','G':'g','B':'b'}
    k = set(['r','g','b'])
    open = set()
    for v in s:
        if v in k:
            open.add(v)
            continue
        elif hm[v] in open:
            continue
        else:
            print("NO")
            break
    else:
        print("YES")