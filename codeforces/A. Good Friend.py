t = int(input())
for i in range (t):
    n = int(input())
    a = list(map(int,input().split()))

    minimum = min(a)
    product = 1
    status = True
    for val in a:
        if status and val == minimum :
            product *= (val + 1)
            status = False
        else:
            product *= val
            
    print (product)