t = int(input())
for _ in range(t):
    n , k = map(int, input().split())
    s = input()
    c0,c1 = 0,0
    for val in s:
        if val == '1':
            c1 += 1
        else:
            c0 +=1
    x = c0//2
    y = c1//2
    if (x + y) >= k:
        z = k - (abs(x - y))
        if z >= 0:
            if z%2 == 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")