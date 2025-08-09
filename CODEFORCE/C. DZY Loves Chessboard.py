n,m = map(int,input().split())
val = []
for i in range(n):
    val.append(list(input()))
    
for i in range(n):

    for j in range(m):
        if val[i][j] == '.':
            if (i+j) % 2 == 0:
                val[i][j] = 'B'
            else:
                val[i][j] = 'W' 

for i in range(n):
    for j in range(m):
        print(val[i][j], end = '')
    print()