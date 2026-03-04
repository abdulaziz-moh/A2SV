import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    zero = [0] * n
    one = [0] * n
    if a[0] ==  '0':
        zero[0] = 1

    for i in range(1,n):
        if a[i] == "0":
            zero[i] = zero[i-1] + 1
        else:
            zero[i] = zero[i-1]
    
    if a[-1] ==  '1':
        one[-1] = 1
    for i in range(n-2, -1, -1):
        if a[i] == '1':
            one[i] = one[i+1] + 1
        else:
            one[i] = one[i+1]

    for i in range(1,n+1):
        if zero[i-1] >= math.ceil(i/2):
            zero[i-1] = i
        else:
            zero[i-1] = None
    
    for i in range(n-1,-1,-1):
        if one[i] >= math.ceil((n-i)/2):
            one[i] = i
        else:
            one[i] = None
            
    ans = [float("inf"),0]
    if one[0] != None:
        ans[0] = n/2
    one.append(n)
    
    for i in range(n):
        
        if zero[i] and one[i+1]:
            if ans[0] > abs((n//2)-(i+1)):
                ans[1] = i+1
                ans[0] = (n/2) - (i+1)
    print(ans[1])
      