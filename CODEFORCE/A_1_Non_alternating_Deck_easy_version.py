t = int(input())
for _ in range(t):
    n = int(input())
    
    i = 0
    alice, bob = 0,0
    while n > 0:
        x = 1 + 8*i
        if n - x >= 0:
            alice += x
            n -= x
        else:
            alice += n
            break
        x = 5 + 8 * i
        if n - x >= 0:
            bob += x
            n -= x
        else:
            bob += n
            break
        i += 1
    print(alice,bob)
        