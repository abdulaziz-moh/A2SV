t = int(input())
for i in range (t):
    n = int(input())
    a = list(map(int,input().split()))
    length = len(a)

    a.sort()
    evenleft,oddleft = 0,0
    left = 0
    right = length

    counteven = 0
    countodd = 0

    while left < length:
        if a[left] % 2 == 0:
            evenleft = left
            counteven += left
            break
    left = 0
    while left < length:
        if a[left] % 2 == 1:
            oddleft = left
            countodd += left
            break
    
    right = length - 1
    while right > evenleft:
        if a[right] % 2 == 0:
            counteven += (length - right - 1)
            break

    right = length
    while right > oddleft:
        if a[right] % 2 == 1:
            countodd += (length - right - 1)
            break
    
    print(min(counteven,countodd))
