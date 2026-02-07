import sys
input_v = sys.stdin.read().split()

n,m = map(int,(input_v[0],input_v[1]))
a = input_v[2]
ptr = 3
hm = {}
for i in range(n):
    if a[i] in hm:
        hm[a[i]].append(i)
    else:
        hm[a[i]] = [i]
print(hm)
for i in range(3,m+3):
    x,y = input_v[ptr],input_v[ptr+1]
    ptr +=2
    