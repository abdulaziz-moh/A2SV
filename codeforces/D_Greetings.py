t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for _ in range(n):
        temp = list(map(int,input().split()))
        a.append(temp)

    count = 0
    for i in range(n-1):
        dxn = (1 if a[i][0] > a[i][1] else -1)
        for j in range(i+1, n):
            x, y = a[j][0], a[j][1]
            newdxn = (1 if x > y else -1)
            if dxn == -1:
                if a[i][0] < x and y < a[i][1] or a[i][0] > x and y > a[i][1] :
                    count+= 1
            elif dxn == 1:
                if a[i][0] > x and y > a[i][1] or a[i][0] < x and y < a[i][1] :
                    count+= 1
            elif dxn != newdxn:
                if a[i][0] < x < y:
                    count += 1
                if x > a[i][0] > a[i][1]:
                    count += 1
    print(count)