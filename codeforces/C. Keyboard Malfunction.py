t = int(input())
for i in range (t):
    s = input()
    newchar = []
    length = len(s)
    i = 0
    while i < length:
        if i+1 == length :
             newchar.append(s[i])
        elif s[i] != s[i +1]:
            newchar.append(s[i])
        else:
            i+=1
        i+=1
    newchar = list(set(newchar))
    newchar.sort()
    s = "".join(newchar)
    print(s)
