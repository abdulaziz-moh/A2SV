t = int(input())
for _ in range(t):
    a,b,c = map(int, input().split())
    x = c + a - (2*b)
    if x >= 0:
        if x % 3 == 0:
            print("YES") 
        else:
            print("NO")
    else:
        print("NO")