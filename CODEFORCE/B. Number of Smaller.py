n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

p1,count = 0,0
ans = []
for v in b:
    while p1<len(a) and a[p1] < v:
        count += 1
        p1 += 1
    print(count, end = " ")

# n,m = map(int,input().split())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))

# l, r = 0, 0
# while l < n and r < m:
#     while l < n and a[l] < b[r]:
#         l += 1
#     print(l,end=" ")
#     r += 1
# while r < m:
#     print(l,end=" ")
#     r += 1