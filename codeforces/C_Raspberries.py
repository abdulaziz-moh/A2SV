import sys
input_v = sys.stdin.read().split()
t =int(input_v[0])
ptr = 1

for _ in range(t):
    n = int(input_v[ptr])
    ptr += 1
    k = int(input_v[ptr])
    ptr += 1
    a = input_v[ptr:ptr+n]
    ptr += n
    
    mn = float("inf")
    for v_s in a:
        v = int(v_s) % k
        x = abs(v - k) % k
        if mn > x:
            mn = x
    print(mn)