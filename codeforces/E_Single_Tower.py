n = int(input())
a, sor= [], []
for _ in range(n):
    x = list(map(int,input().split()))
    a.append(x)
    sor.extend(x[1:])
    
sor.sort(reverse=True)
hm = {}
for i in range(len(sor)-1):
    hm[sor[i]] = sor[i+1]
hm[sor[-1]] = -1 
s,c = 0,n-1
for v in a:
    for i in range(v[0], 1,-1):
        if hm[v[i]] != v[i-1]:
            s+=1
            c+=1
print(s,c)
        



























    
    
    
    
    
    
# s,c = 0,0
# x = []
# for i in range(n):
#     z = 1
#     for j in range(1,a[i][0]):
#         if a[i][j] > a[i][j+1]:
#             x.append(a[i][z:j+1])
#             z = j+1
#             s += 1
#             c += 1
#     if a[i][z:]:
#         x.append(a[i][z:])
# x.sort(key= lambda x:x[-1])
# print(x)
# for i in range(len(x)-1):
#     if x[i][-1] < x[i+1][-1] and x[i][1] > x[i+1][1]:
#         s += 1
#         c += 2
    
#     elif len(x[i]) > 1 and len(x[i+1]) > 1 and x[i][-1] < x[i+1][-1] and x[i][1] < x[i+1][1]:
#         s += 2
#         c += 2
    
# c += (n-1)
# print(s,c)
