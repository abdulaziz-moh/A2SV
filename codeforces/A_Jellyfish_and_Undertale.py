import sys
input_v = sys.stdin.read().split()

t = int(input_v[0])
ptr = 1

for _ in range(t):
    a,b,n = map(int,input_v[ptr:ptr+3])
    ptr += 3
    x = list(map(int,input_v[ptr:ptr+n]))
    ptr += n
    
    sum = b
    for v in x:
        sum += min(v,a-1)
    print(sum)