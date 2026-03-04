t = int(input())
for _ in range(t):
    n, m  = map(int,input().split())
    arr = []
    for _ in range(n):
        imp = input()
        a = []
        for v in imp:
            a.append(int(v))
        arr.append(a)
    count = 0
    loop = min(m,n)//2
    stack = [3,4,5,1]
    
    i = 0
    while i < loop:
        
        # To Right mov't at the Top
        for j in range(i,m-i):
            if arr[i][j] == stack[-1]:
                arr[i][j] = 0
                stack.pop()
                if not stack:
                    arr[i][j] = 0
                    count += 1
                    stack = [3,4,5,1]
            else:
                # check this case for the use of this 
                # 2 4
                # 3001
                # 4515
                stack = [3,4,5,1]
                if arr[i][j] == stack[-1]:  
                    arr[i][j] = 0
                    stack.pop()
                    
        # To Down mov't at the Right
        for j in range(i+1,n-1-i):
            if arr[j][m-1-i] == stack[-1]:
                arr[j][m-1-i] = 0
                stack.pop()
                if not stack:
                    arr[j][m-1-i] = 0
                    count += 1
                    stack = [3,4,5,1]                
            else:
                stack = [3,4,5,1]
                if arr[j][m-1-i] == stack[-1]:
                    arr[j][m-1-i] = 0
                    stack.pop()
                
                    
        # To Left mov't at the bottom
        for j in range(m-1-i, i-1, -1):
            if arr[n-1-i][j] == stack[-1]:
                arr[n-1-i][j] = 0
                stack.pop()
                if not stack:
                    arr[n-1-i][j] = 0
                    count += 1
                    stack = [3,4,5,1]
            else:
                stack = [3,4,5,1]
                if arr[n-1-i][j] == stack[-1]:
                    arr[n-1-i][j] = 0
                    stack.pop()
        
        # To Up mov't at the Left
        for j in range(n-2-i, i, -1):
            if arr[j][i] == stack[-1]:
                arr[j][i] = 0
                stack.pop()
                if not stack:
                    arr[j][i] = 0
                    count += 1
                    stack = [3,4,5,1]
            else:
                stack = [3,4,5,1]
                if arr[j][i] == stack[-1]:
                    arr[j][i] = 0
                    stack.pop()
        # Check if some sequence begin at the end of the loop need to continue again at form the start in the same cycle level
        if len(stack) < 4:
            continue
        i += 1
    print(count)