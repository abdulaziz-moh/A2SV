t = int(input())

for i in range(t):
    a = input()
    n = len(a)
        
    count = [1]
    for i in range(1,n):
        
        if a[i] == a[i-1]:
            if a[i] == '<' or a[i] == '>':
                count[-1] += 1
            else:
                count.append(-1)
                break
        elif a[i] == '<' and a[i-1] == '>':
            count.append(-1)
            break
        elif a[i] == '>' and a[i-1] == '<':
            count.append(1)
                    
        elif a[i] == '*' and a[i-1] == '>':
            count.append(-1)
            break
        elif a[i] == '*' and a[i-1] == '<':
            count[-1] += 1
        
        elif a[i] == '<' and a[i-1] == '*':
            count.append(-1)
            break
        elif a[i] == '>' and a[i-1] == '*':
            count.append(2)
              
    if count[-1] == -1:
        print("-1")
    else:  
        print(str(max(count)))   