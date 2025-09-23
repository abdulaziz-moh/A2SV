n = int(input())
count,i = 0,0
bill = [100,20,10,5,1]
while n != 0:
    if n >= bill[i]:
        add = n//bill[i]
        n = n%bill[i]
        count += add
    else:
        i += 1
print(count)