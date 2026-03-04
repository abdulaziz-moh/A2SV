t = int(input())
for _ in range(t):
    n = int(input())
    
    i = 0
    alicew, bobw ,aliceb, bobb= 0,0,0,0
    while n > 0:
        x = 1 + 8*i
        if n - x >= 0:
            alicew += 1+4*i
            aliceb += 4 * i
            n -= x
        else:
            alicew += n//2 + n%2
            aliceb += n//2 
            break
        x = 5 + 8 * i
        if n - x >= 0:
            bobw += 2 + 4*i
            bobb += 3 + 4*i
            n -= x
        else:
            bobw += n//2
            bobb += n//2 + n%2
            break
        i += 1
    print(alicew, aliceb,bobw,bobb)
        