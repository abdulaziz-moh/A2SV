import sys
input_v = sys.stdin.read().split()
t = int(input_v[0])
ptr = 1

for i in range(t):
    # print("i: ",i+1)
    n = int(input_v[ptr])
    ptr += 1
    count = 0
    for _ in range(n):
        a,b,c,d = map(int,input_v[ptr:ptr+4])
        ptr += 4
        suba = a - c
        subb = b - d
        # print(a,b,c,d," ",suba,subb)
        if suba > 0:
            count += suba
        if subb > 0 and suba >= 0:
            count += c + subb
        elif subb > 0 and suba < 0:
            count += a + subb
        elif subb > 0:
            count += subb
    print(count)