status = True
idx = [0,0]
for i in range(1,6):
    if status:
        a = list(map(int,input().split()))
        for j in range(1,6):
            if a[j-1] == 1:
                idx = [i,j]
                status = False
                break
    else:
        input()
print(abs(3-idx[0]) + abs(3-idx[1]))