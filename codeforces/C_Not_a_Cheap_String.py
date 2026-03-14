from collections import defaultdict


t = int(input())
for _ in range(t):
    s = input()
    p = int(input())
    
    a, hm = [], defaultdict(int)
    offset, sum = ord('a'), 0
    for v in s:
        x = ord(v) - offset + 1
        a.append(x)
        hm[v] += 1
        sum += x
    a.sort(reverse=True)
    
    for v in a:
        if sum > p:
            sum -= v
            x = chr(offset + v - 1)
            hm[x] -= 1
            if hm[x] == 0:
                del hm[x]
        else:
            break
    x = [] 
    for v in s:
        if v in hm:
            x.append(v)
            hm[v] -= 1
            if hm[v] == 0:
                del hm[v]
    print("".join(x))