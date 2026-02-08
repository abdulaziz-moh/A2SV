t = int(input())
for _ in range(t):
    ab = input()
    status = False
    n = len(ab)
    r = 1
    if n == 2 and int(ab[0:r]) < int(ab[r:]):
            status = True
    
    while r < n-1:
        while ab[r] == '0' and r < n-1:
            r += 1
        if int(ab[0:r]) < int(ab[r:]):
            status = True
            break
        r += 1
    if status:
        print(ab[:r]+" "+ab[r:])
    else:
        print('-1')