# t = int(input())
# for i in range(t):
#     n,k = map(int, input().split())
#     status = True
#     s = n-k+1
#     e = n+1
#     for j in range(s,e):
#         if (j**2)/2 != 0:
#             status = False
#             break
#     if status:
#         print("YES")
#     else:
#         print("NO")

def sum_of_squares(x):
    return x * (x + 1) * (2 * x + 1) // 6

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l = max(1, n - k + 1)
    r = n
    total = sum_of_squares(r) - sum_of_squares(l - 1)
    if total % 2 == 0:
        print("YES")
    else:
        print("NO")