from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    mn = float('inf')

    idx = []
    for i in range(n):
        if s[i] == 'a':
            idx.append(i)
    l = len(idx)
    for i in range(l-1):
        count = defaultdict(int)
        for j in range(idx[i],min(n, idx[i]+7)):
            count[s[j]] += 1
            
            if j- idx[i]+1 > 1 and count['a'] > max(count['b'],count['c']):
                mn = min(mn, j-idx[i]+1)
                break
    if mn == float('inf'):
        print(-1)
    else:
        print(mn)
        

    # for i in range(n-1):
    #     count = defaultdict(int)
    #     for j in range(i,min(n,i+7)):
    #         count[s[j]] += 1
            
    #         if j-i+1 > 1 and count['a'] > max(count['b'],count['c']):
    #             mn = min(mn, j-i+1)
    #             break
                        
    # if mn == float("inf"):
    #     print(-1)
    # else:
    #     print(mn)
    