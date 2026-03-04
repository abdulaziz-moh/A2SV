t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    newchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = [0] *26
    
    
    s = []
    for i in range(len(a)):
        j = 0
        while count[j] != a[i]:
            j += 1
        s.append(newchar[j])
        count[j] += 1
            
    print("".join(s))
    
    
# ------------------------------------------------------------------------------------------

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int,input().split()))
#     newchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     count = 0
    
#     s = []
#     for i in range(len(a)):
#         if a[i] == 0:
#             s.append(newchar[count])
#             a[i] += 1
#             count += 1
#         else:
#             for j in range(i):
#                 if a[i] == a[j]:
#                     s.append(s[j])
#                     a[j] += 1
#                     a[i] = a[j]
#                     break
#     print("".join(s))
