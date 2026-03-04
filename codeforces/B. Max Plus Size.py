t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    max = 0

    max_indexes = []
    even, odd = 0,0
    if n%2 == 0:
        even = odd = int(n/2)
    else:
        odd = n//2
        even = (n//2) + 1
    
    for j in range(n):
        if nums[j] == max:
            max_indexes.append(j)
        elif nums[j] > max:
            max_indexes.clear()
            max = nums[j]
            max_indexes.append(j)
    status = False
    for val in max_indexes:
        if val%2 == 0:
            status = True
            break
    
    ans = max
    if even > odd and status:
        ans = print(max + even)
    else:
        print(max + odd)
