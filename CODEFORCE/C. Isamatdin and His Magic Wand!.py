# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int,input().split()))
    
#     rem = []
#     for i in range(n):
#         if a[i] % 2 != 0:
#             rem.append(1)
#         else:
#             rem.append(0)
#     for i in range(n-1):
#         for j in range(i+1,n):
#             if a[i] > a[j] and rem[i] != rem[j]:
#                 a[i],a[j] = a[j],a[i]
#                 rem[i],rem[j] = rem[j],rem[i]
#     print(*a)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    odds = sorted([x for x in a if x % 2 == 1])
    evens = sorted([x for x in a if x % 2 == 0])
    
    oi = ei = 0
    result = []
    for x in a:
        if x % 2 == 1:
            result.append(odds[oi])
            oi += 1
        else:
            result.append(evens[ei])
            ei += 1
    
    print(*result)
