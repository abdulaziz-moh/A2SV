t = int(input())
for i in range (t):
    a = input()
    newchar = []
    length = len(a)
    for i in range(length):
        if a[i] == 'p':
            newchar.append('q') 
        elif a[i] == 'q':
            newchar.append('p')
        else:
            newchar.append('w')
    a = "".join(newchar)
    print (a)

