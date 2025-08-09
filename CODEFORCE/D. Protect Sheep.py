r,c = map(int,input().split())
val = []
for i in range(r):
    val.append(list(input()))

status = True
pos = [[-1,0],[0,1],[1,0],[0,-1]]
for i in range(r):
    for j in range(c):
        if val[i][j] == 'W':           
            for dx,dy in pos:
                x,y = dx+i, dy+j                
                if 0 <= x < r and 0 <= y < c :
                    if val[x][y] == 'S':
                        print('NO')
                        status = False
                        break
                    elif val[x][y] == '.':
                        val[x][y]  = 'D'
        if not status:
            break
    if not status:
        break     
if status:
    print('YES')
    for i in range(r):
        for j in range(c):
            print(val[i][j], end = '')
        print()
                    