# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int,input().split()))
#     hm = {}
#     unq = []
#     for v in a:
#         if v not in hm:
#             hm[v] = 1
#             unq.append(v)  
#     for i in range(1,n+1):
#         if i not in hm:
#             unq.append(i)
#     for i in range(n):
#         print(unq[i], end=' ')
#     print()
#     # print(*unq)

import sys
input_data = sys.stdin.read().split()

ptr = 0
t = int(input_data[ptr])
ptr += 1

results = []
for _ in range(t):
    n = int(input_data[ptr])
    ptr += 1
    a = list(map(int,input_data[ptr:ptr+n]))
    ptr += n
    
    ans = []
    used = [False] * (n+1)
    unused_ptr = 1
    for v_str in a:
        v = int(v_str)
        if not used[v]:
            ans.append(v)
            used[v] = True
        else:
            while unused_ptr <= n and used[unused_ptr]:
                unused_ptr += 1
            ans.append(unused_ptr)
            used[unused_ptr] = True
            
    results.append(" ".join(map(str,ans)))
sys.stdout.write("\n".join(results) + "\n")