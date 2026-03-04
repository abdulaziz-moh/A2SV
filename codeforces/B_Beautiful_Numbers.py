t = int(input())
for _ in range(t):
    x = input()
    first = int(x[0])
    fcount = 0
    sum = 0
    lst = []
    
    for v in x:
        lst.append(int(v))
        sum += int(v)
        if int(v) == first:
             fcount += 1
        
    if sum < 10:
        print(0)
    else:       
        lst.sort()
        count, n = 0, len(lst)
        i = n - 1
        status = True
        while i >= 0 and sum >= 10:
            if status and lst[i] == first:
                if fcount == 1:
                    sum += 1
                    status = False
                else:
                    fcount -= 1
                
            sum -= lst[i]
            i -= 1
            count += 1
        
        print(count)