import sys
input_v = sys.stdin.read().split()

t = int(input_v[0])
ptr = 1

for _ in range(t):
    s = input_v[ptr]
    ptr += 1
    z,o = 0,0
    for v in s:
        if v == '0':
            z += 1
        else:
            o += 1
    ans = 0
    for v in s:
        if v == "0" and o > 0:
            o -= 1
        elif v == "1" and z > 0:
            z -= 1
        else:
            break
        ans += 1
    print(len(s) - ans)