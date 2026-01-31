import sys
input_v = sys.stdin.readline()
s = input_v

a = ['o','l','l','e','h']
n = len(s)
i = 0
j = 4
while j >= 0 and i < n:
    if s[i] == a[j]:
        j -= 1
    i += 1
if j == -1:
    print('YES')
else:
    print("NO")