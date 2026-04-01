
n = int(input())
s = input()

l, o = [0], [0]
ocount, lcount = 0, 0
for v in s:
    if v == 'O':
        o.append(o[-1]+1)
        l.append(l[-1])
        ocount += 1
    else:
        o.append(o[-1])
        l.append(l[-1] + 1)
        lcount += 1
# print(o)
# print(l)
for i in range(1,n+1):
    if ocount - o[i] != o[i] and lcount - l[i] != l[i]:
        s1 = ocount - o[i] + lcount - l[i]
        s2 = o[i] + l[i]
        # print(s1, " ", s2)
        if s1> 0 and s2> 0:
            print(s2)
            break
else:
    print(-1)
        