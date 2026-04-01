
n = int(input())
a = list(map(int,input().split()))
a.append(0)
temp = [sum(a)]
summ = temp[0]
temp.append(temp[0]/2)
ans = [float('inf')]
x = [0]

def backtrack(left):
    global summ
    if left > n:
        # ans[0] = min(ans[0], int(abs(x[0]-temp[1])*2))
        ans[0] = min(ans[0], int(abs(summ- 2 * (x[0]))))

        return
    
    for i in range(left, n+1):

        x[0] += a[i]
        # if abs(x[0] - temp[1]) >= ans[0]:
        #     continue
        
        backtrack(i + 1)
        x[0] -= a[i]
        
backtrack(0)
print(ans[0])