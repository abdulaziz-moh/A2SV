t = int(input())
 
for i in range(t):
 
    val = list(map(int,input().split()))
 
    if val[0] == val[1] + val[2] or val[1] == val[0] + val[2] or val[2] == val[0] + val[1]:
        print("YES")
    else:
        print ("NO")