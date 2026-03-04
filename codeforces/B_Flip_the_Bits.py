from typing import Counter


for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    
    reverse = {'0':'1', '1':'0'}
    count = Counter(a)
    invert = 0
    for i in range(n-1, -1, -1):
        check = a[i] if invert % 2 == 0 else reverse[a[i]]
        if check != b[i]:
            if count['0'] != count['1']:
                print('NO')
                break
            invert += 1
        if invert % 2 == 0:
            count[a[i]] -= 1
        else:
            count[reverse[a[i]]] -= 1
    else:
        print('YES')