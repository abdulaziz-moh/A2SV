n,q,m = map(int,input().split())
a = list(map(int,input().split()))
que = []
for _ in range(q):
    x = list(map(int,input().split()))
    que.append(x)
b = list(map(int,input().split()))
ans = []

for v in b:
    B = v
    for i in range(len(que)-1,-1,-1):
        if B <= que[i][2] and B >= que[i][1]:

            if que[i][0] == 1:
                if B != que[i][1]:
                    B -= 1
                else:
                    B = que[i][2]
            else:
                B = que[i][2] - B + que[i][1] 
                
    ans.append(a[B-1])

print(*ans)
                